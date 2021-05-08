#' ---
#' title: malha fundiaria analises
#' author: mauricio vancine
#' date: 2020-12-02
#' ---

# packages ----------------------------------------------------------------
library(tidyverse)
library(here)
library(sf)
library(raster)

# options
options(scipen = 1e5, warn = -1)

# tabelas
malha_tabela <- readr::read_csv(here::here("10_malha_fundiaria", "tables",
                                           "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora.csv")) %>% 
  dplyr::rename(malha_classe = classe, malha_subclasse = subclasse)
malha_tabela

uso_tabela <- tibble::tibble(valor = 1:5, 
                             uso_classe = c("Floresta", "Savana", "Silvicultura", "Antrópico", "Água"))
uso_tabela

prop_tabela <- tibble::tibble(valor = 0:1, 
                           prop_classe = c("Propriedade Suzano", "Não-propriedade Suzano"))
prop_tabela

# bamges ------------------------------------------------------------------
# import data
bamges_buffer500m <- sf::st_read(here::here("07_corredores_buffer500m", "bamges", "corr_bamges_buffer500m.shp"))
bamges_buffer500m
plot(bamges_buffer500m$geometry)

uso_buffer500m_bamges <- raster::raster(here::here("10_malha_fundiaria", "bamges", 
                                                   "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_bamges_buffer500m.tif"))
names(uso_buffer500m_bamges) <- "uso"
uso_buffer500m_bamges
plot(uso_buffer500m_bamges)

prop_buffer500m_bamges <- raster::raster(here::here("10_malha_fundiaria", "bamges", 
                                                    "suzano_properties_30m_inside_bamges_bin_buffer500m.tif"))
names(prop_buffer500m_bamges) <- "prop"
prop_buffer500m_bamges
plot(prop_buffer500m_bamges)

malha_buffer500m_bamges <- raster::raster(here::here("10_malha_fundiaria", "bamges", 
                                                     "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges_albers_30m_buffer500m.tif"))
names(malha_buffer500m_bamges) <- "malha"
malha_buffer500m_bamges
plot(malha_buffer500m_bamges)

# stack
bamges <- raster::stack(uso_buffer500m_bamges, prop_buffer500m_bamges, malha_buffer500m_bamges) %>% 
  raster::crop(bamges_buffer500m) %>%
  raster::mask(bamges_buffer500m) %>% 
  raster::values() %>% 
  tibble::as_tibble() %>% 
  tidyr::drop_na()
bamges

bamges_summary <- bamges %>% 
  dplyr::group_by(prop, malha, uso) %>% 
  dplyr::summarise(area_ha = n() * 0.09)
bamges_summary

# legenda
bamges_summary_legend <- bamges_summary %>% 
  dplyr::left_join(prop_tabela, by = c("prop" = "valor")) %>%
  dplyr::left_join(uso_tabela, by = c("uso" = "valor")) %>% 
  dplyr::left_join(malha_tabela, by = c("malha" = "valor")) %>% 
  tibble::tibble() %>% 
  dplyr::select(prop_classe, malha_classe, malha_subclasse, uso_classe, area_ha)
bamges_summary_legend

# export
readr::write_csv(bamges_summary_legend, here::here("10_malha_fundiaria", "malha_fundiaria_buffer500m_bamges_summary_legend.csv"))


# ma ------------------------------------------------------------------
# import data
ma_buffer500m <- sf::st_read(here::here("07_corredores_buffer500m", "ma", "corr_ma_buffer500m.shp"))
ma_buffer500m
plot(ma_buffer500m$geometry)

uso_buffer500m_ma <- raster::raster(here::here("10_malha_fundiaria", "ma", 
                                               "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_ma_buffer500m.tif"))
names(uso_buffer500m_ma) <- "uso"
uso_buffer500m_ma
plot(uso_buffer500m_ma)

prop_buffer500m_ma <- raster::raster(here::here("10_malha_fundiaria", "ma", 
                                                "suzano_properties_30m_inside_ma_bin_buffer500m.tif"))
names(prop_buffer500m_ma) <- "prop"
prop_buffer500m_ma
plot(prop_buffer500m_ma)

malha_buffer500m_ma <- raster::raster(here::here("10_malha_fundiaria", "ma", 
                                                 "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma_albers_30m_buffer500m.tif"))
names(malha_buffer500m_ma) <- "malha"
malha_buffer500m_ma
plot(malha_buffer500m_ma)

# stack
ma <- raster::stack(uso_buffer500m_ma, prop_buffer500m_ma, malha_buffer500m_ma) %>% 
  raster::crop(ma_buffer500m) %>%
  raster::mask(ma_buffer500m) %>% 
  raster::values() %>% 
  tibble::as_tibble() %>% 
  tidyr::drop_na()
ma

ma_summary <- ma %>% 
  dplyr::group_by(prop, malha, uso) %>% 
  dplyr::summarise(area_ha = n() * 0.09)
ma_summary

# legenda
ma_summary_legend <- ma_summary %>% 
  dplyr::left_join(prop_tabela, by = c("prop" = "valor")) %>%
  dplyr::left_join(uso_tabela, by = c("uso" = "valor")) %>% 
  dplyr::left_join(malha_tabela, by = c("malha" = "valor")) %>% 
  tibble::tibble() %>% 
  dplyr::select(prop_classe, malha_classe, malha_subclasse, uso_classe, area_ha)
ma_summary_legend

# export
readr::write_csv(ma_summary_legend, here::here("10_malha_fundiaria", "malha_fundiaria_buffer500m_ma_summary_legend.csv"))


# ms ------------------------------------------------------------------
# import data
ms_buffer500m <- sf::st_read(here::here("07_corredores_buffer500m", "ms", "corr_ms_buffer500m.shp"))
ms_buffer500m
plot(ms_buffer500m$geometry)

uso_buffer500m_ms <- raster::raster(here::here("10_malha_fundiaria", "ms", 
                                               "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_ms_buffer500m.tif"))
names(uso_buffer500m_ms) <- "uso"
uso_buffer500m_ms
plot(uso_buffer500m_ms)

prop_buffer500m_ms <- raster::raster(here::here("10_malha_fundiaria", "ms", 
                                                "suzano_properties_30m_inside_ms_bin_buffer500m.tif"))
names(prop_buffer500m_ms) <- "prop"
prop_buffer500m_ms
plot(prop_buffer500m_ms)

malha_buffer500m_ms <- raster::raster(here::here("10_malha_fundiaria", "ms", 
                                                 "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms_albers_30m_buffer500m.tif"))
names(malha_buffer500m_ms) <- "malha"
malha_buffer500m_ms
plot(malha_buffer500m_ms)

# stack
ms <- raster::stack(uso_buffer500m_ms, prop_buffer500m_ms, malha_buffer500m_ms) %>% 
  raster::crop(ms_buffer500m) %>%
  raster::mask(ms_buffer500m) %>% 
  raster::values() %>% 
  tibble::as_tibble() %>% 
  tidyr::drop_na()
ms

ms_summary <- ms %>% 
  dplyr::group_by(prop, malha, uso) %>% 
  dplyr::summarise(area_ha = n() * 0.09)
ms_summary

# legenda
ms_summary_legend <- ms_summary %>% 
  dplyr::left_join(prop_tabela, by = c("prop" = "valor")) %>%
  dplyr::left_join(uso_tabela, by = c("uso" = "valor")) %>% 
  dplyr::left_join(malha_tabela, by = c("malha" = "valor")) %>% 
  tibble::tibble() %>% 
  dplyr::select(prop_classe, malha_classe, malha_subclasse, uso_classe, area_ha)
ms_summary_legend

# export
readr::write_csv(ms_summary_legend, here::here("10_malha_fundiaria", "malha_fundiaria_buffer500m_ms_summary_legend.csv"))


# end ---------------------------------------------------------------------