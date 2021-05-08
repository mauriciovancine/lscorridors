#' ---
#' title: malha fundiaria analises
#' author: mauricio vancine
#' date: 2020-12-08
#' ---

# packages ----------------------------------------------------------------
library(tidyverse)
library(here)
library(sf)
library(raster)

# options
options(scipen = 1e5, warn = -1)

# bamges --------------------------------------------------------------------
# directory
setwd("/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/12_malha_fundiaria/bamges")

# import
malha_bamges <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_bamges_topologia_malha_join.shp")
malha_bamges

plot(malha_bamges$geometry)

dim(malha_bamges)

# area
malha_bamges_area <- malha_bamges %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.)/1e4, 2)))
malha_bamges_area

# agregar numero
malha_bamges_area_agg <- malha_bamges_area %>% 
  sf::st_drop_geometry() %>% 
  dplyr::filter(area_ha >= 1, 
                value == 4,
                classe %in% c("Terra privada", "Terra pública")) %>% 
  dplyr::group_by(classe, id_imovel) %>% 
  dplyr::summarise(n = n(), area_ha = sum(area_ha)) %>% 
  dplyr::group_by(classe) %>% 
  dplyr::summarise(n = n(), area_ha = sum(area_ha))
malha_bamges_area_agg

# ma --------------------------------------------------------------------
# directory
setwd("/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/12_malha_fundiaria/ma")

# import
malha_ma <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_ma_topologia_malha_join.shp")
malha_ma

plot(malha_ma$geometry)

dim(malha_ma)

# area
malha_ma_area <- malha_ma %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.)/1e4, 2)))
malha_ma_area

# agregar numero
malha_ma_area_agg <- malha_ma_area %>% 
  sf::st_drop_geometry() %>% 
  dplyr::filter(area_ha >= 1, 
                value == 4,
                classe %in% c("Terra privada", "Terra pública")) %>% 
  dplyr::group_by(classe, id_imovel) %>% 
  dplyr::summarise(n = n(), area_ha = sum(area_ha)) %>% 
  dplyr::group_by(classe) %>% 
  dplyr::summarise(n = n(), area_ha = sum(area_ha))
malha_ma_area_agg

# ms --------------------------------------------------------------------
# directory
setwd("/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/12_malha_fundiaria/ms")

# import
malha_ms <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_ms_topologia_malha_join.shp")
malha_ms

plot(malha_ms$geometry)

dim(malha_ms)

# area
malha_ms_area <- malha_ms %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.)/1e4, 2)))
malha_ms_area

# agregar numero
malha_ms_area_agg <- malha_ms_area %>% 
  sf::st_drop_geometry() %>% 
  dplyr::filter(area_ha >= 1, 
                value == 4,
                classe %in% c("Terra privada", "Terra pública")) %>% 
  dplyr::group_by(classe, id_imovel) %>% 
  dplyr::summarise(n = n(), area_ha = sum(area_ha)) %>% 
  dplyr::group_by(classe) %>% 
  dplyr::summarise(n = n(), area_ha = sum(area_ha))
malha_ms_area_agg


# export
analysis <- rbind(malha_bamges_area_agg,
malha_ma_area_agg,
malha_ms_area_agg) %>% 
  mutate(local = c("BAMGES", "BAMGES", "MA", "MA", "MS"), .before = 1)
analysis

readr::write_csv(analysis, "00_analysis_malha_fundiaria_antropico.csv")

# end ---------------------------------------------------------------------