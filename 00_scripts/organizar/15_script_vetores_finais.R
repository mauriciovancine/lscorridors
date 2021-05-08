#' ---
#' title: vetores finais
#' author: mauricio vancine
#' date: 2020-12-16
#' ---

# packages ----------------------------------------------------------------
library(tidyverse)
library(sf)
library(raster)

# options
options(scipen = 1e5, warn = -1)

# bamges --------------------------------------------------------------------
# directory
setwd("/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/13_vetores_finais/bamges")

# fragmentos ----
bamges_frag <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m.shp")
bamges_frag

plot(bamges_frag$geometry, col = "gray")
dim(bamges_frag)

bamges_frag$area_ha %>% sum

# corredor uso total ----
bamges_corr_uso <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer250m_bamges.shp")
bamges_corr_uso

plot(bamges_corr_uso$geometry, col = "gray")
dim(bamges_corr_uso)

# area
bamges_corr_uso <- bamges_corr_uso %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.), 2)))
bamges_corr_uso

# aggregate
bamges_corr_uso %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(value) %>% 
  dplyr::summarise(area = sum(area_ha)) %>% 
  dplyr::mutate(por = (area/sum(area))*100)


# corredor uso inside ----
bamges_corr_uso_inside <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer250m_bamges_inside.shp")
bamges_corr_uso_inside

plot(bamges_corr_uso_inside$geometry, col = "gray")
dim(bamges_corr_uso_inside)

# area
bamges_corr_uso_inside <- bamges_corr_uso_inside %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.), 2)))
bamges_corr_uso_inside

# aggregate
bamges_corr_uso_inside %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(value) %>% 
  dplyr::summarise(area = sum(area_ha)) %>% 
  dplyr::mutate(por = (area/sum(area))*100)


# corredor uso outside ----
bamges_corr_uso_outside <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer250m_bamges_outside.shp")
bamges_corr_uso_outside

plot(bamges_corr_uso_outside$geometry, col = "gray")
dim(bamges_corr_uso_outside)

# area
bamges_corr_uso_outside <- bamges_corr_uso_outside %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.), 2)))
bamges_corr_uso_outside

# aggregate
bamges_corr_uso_outside %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(value) %>% 
  dplyr::summarise(area = sum(area_ha)) %>% 
  dplyr::mutate(por = (area/sum(area))*100)



# ma --------------------------------------------------------------------
# directory
setwd("/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/13_vetores_finais/ma")

# fragmentos ----
ma_frag <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m.shp")

dim(ma_frag)

ma_frag %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by() %>% 
  dplyr::summarise(area = sum(area_ha),
                   area_r = sum(area_ha_r))

# corredor uso total ----
ma_corr_uso <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer250m_ma.shp")
ma_corr_uso

plot(ma_corr_uso$geometry, col = "gray")
dim(ma_corr_uso)

# area
ma_corr_uso <- ma_corr_uso %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.), 2)))
ma_corr_uso

# aggregate
ma_corr_uso %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(value) %>% 
  dplyr::summarise(area = sum(area_ha)) %>% 
  dplyr::mutate(por = (area/sum(area))*100)


# corredor uso inside ----
ma_corr_uso_inside <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer250m_ma_inside.shp")
ma_corr_uso_inside

plot(ma_corr_uso_inside$geometry, col = "gray")
dim(ma_corr_uso_inside)

# area
ma_corr_uso_inside <- ma_corr_uso_inside %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.), 2)))
ma_corr_uso_inside

# aggregate
ma_corr_uso_inside %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(value) %>% 
  dplyr::summarise(area = sum(area_ha)) %>% 
  dplyr::mutate(por = (area/sum(area))*100)


# corredor uso outside ----
ma_corr_uso_outside <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer250m_ma_outside.shp")
ma_corr_uso_outside

plot(ma_corr_uso_outside$geometry, col = "gray")
dim(ma_corr_uso_outside)

# area
ma_corr_uso_outside <- ma_corr_uso_outside %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.), 2)))
ma_corr_uso_outside

# aggregate
ma_corr_uso_outside %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(value) %>% 
  dplyr::summarise(area = sum(area_ha)) %>% 
  dplyr::mutate(por = (area/sum(area))*100)


# ms --------------------------------------------------------------------
# directory
setwd("/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/13_vetores_finais/ms")

# fragmentos ----
ms_frag <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m.shp")
ms_frag

plot(ms_frag$geometry, col = "gray")
dim(ms_frag)

ms_frag$area_ha %>% sum

# corredor uso total ----
ms_corr_uso <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer250m_ms.shp")
ms_corr_uso

plot(ms_corr_uso$geometry, col = "gray")
dim(ms_corr_uso)

# area
ms_corr_uso <- ms_corr_uso %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.), 2)))
ms_corr_uso

# aggregate
ms_corr_uso %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(value) %>% 
  dplyr::summarise(area = sum(area_ha)) %>% 
  dplyr::mutate(por = (area/sum(area))*100)


# corredor uso inside ----
ms_corr_uso_inside <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer250m_ms_inside.shp")
ms_corr_uso_inside

plot(ms_corr_uso_inside$geometry, col = "gray")
dim(ms_corr_uso_inside)

# area
ms_corr_uso_inside <- ms_corr_uso_inside %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.), 2)))
ms_corr_uso_inside

# aggregate
ms_corr_uso_inside %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(value) %>% 
  dplyr::summarise(area = sum(area_ha)) %>% 
  dplyr::mutate(por = (area/sum(area))*100)


# corredor uso outside ----
ms_corr_uso_outside <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer250m_ms_outside.shp")
ms_corr_uso_outside

plot(ms_corr_uso_outside$geometry, col = "gray")
dim(ms_corr_uso_outside)

# area
ms_corr_uso_outside <- ms_corr_uso_outside %>% 
  dplyr::mutate(area_ha = as.numeric(round(sf::st_area(.), 2)))
ms_corr_uso_outside

# aggregate
ms_corr_uso_outside %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(value) %>% 
  dplyr::summarise(area = sum(area_ha)) %>% 
  dplyr::mutate(por = (area/sum(area))*100)

# end ---------------------------------------------------------------------