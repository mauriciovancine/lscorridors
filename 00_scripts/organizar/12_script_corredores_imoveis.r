#' ---
#' title: corredores fragmentos e imoveis
#' author: mauricio vancine
#' date: 2020-12-09
#' ---

# packages
library(sf)
library(tidyverse)

# bamges ------------------------------------------------------------------
# directory
setwd("/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/10_corredores_imoveis/bamges")

# bamges inside 45m -----
bamges_in_45m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_inside_imoveis.shp")

bamges_in_45m_group <- bamges_in_45m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
bamges_in_45m_group$area_ha %>% sum
bamges_in_45m_group$area_ha_r %>% sum


# bamges outside 45m -----
bamges_out_45m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_outside_imoveis.shp")

bamges_out_45m_group <- bamges_out_45m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
bamges_out_45m_group$area_ha %>% sum
bamges_out_45m_group$area_ha_r %>% sum


# bamges inside 250m -----
bamges_in_250m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_inside_imoveis.shp")


bamges_in_250m_group <- bamges_in_250m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
bamges_in_250m_group$area_ha %>% sum
bamges_in_250m_group$area_ha_r %>% sum


# bamges outside 250m -----
bamges_out_250m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_outside_imoveis.shp")

bamges_out_250m_group <- bamges_out_250m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
bamges_out_250m_group$area_ha %>% sum
bamges_out_250m_group$area_ha_r %>% sum

# bamges inside 500m -----
bamges_in_500m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_inside_imoveis.shp")

bamges_in_500m_group <- bamges_in_500m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
bamges_in_500m_group$area_ha %>% sum
bamges_in_500m_group$area_ha_r %>% sum

# bamges outside 500m -----
bamges_out_500m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_outside_imoveis.shp")

bamges_out_500m_group <- bamges_out_500m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
bamges_out_500m_group$area_ha %>% sum
bamges_out_500m_group$area_ha_r %>% sum


# ma ------------------------------------------------------------------
# directory
setwd("/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/10_corredores_imoveis/ma")

# ma inside 45m -----
ma_in_45m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_inside_imoveis.shp")

ma_in_45m_group <- ma_in_45m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ma_in_45m_group$area_ha %>% sum
ma_in_45m_group$area_ha_r %>% sum


# ma outside 45m -----
ma_out_45m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_outside_imoveis.shp")

ma_out_45m_group <- ma_out_45m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ma_out_45m_group$area_ha %>% sum
ma_out_45m_group$area_ha_r %>% sum

# ma inside 250m -----
ma_in_250m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_inside_imoveis.shp")
ma_in_250m

ma_in_250m_group <- ma_in_250m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ma_in_250m_group$area_ha %>% sum
ma_in_250m_group$area_ha_r %>% sum


# ma outside 250m -----
ma_out_250m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_outside_imoveis.shp")

ma_out_250m_group <- ma_out_250m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ma_out_250m_group$area_ha %>% sum
ma_out_250m_group$area_ha_r %>% sum

# ma inside 500m -----
ma_in_500m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_inside_imoveis.shp")

ma_in_500m_group <- ma_in_500m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ma_in_500m_group$area_ha %>% sum
ma_in_500m_group$area_ha_r %>% sum

# ma outside 500m -----
ma_out_500m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_outside_imoveis.shp")

ma_out_500m_group <- ma_out_500m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ma_out_500m_group$area_ha %>% sum
ma_out_500m_group$area_ha_r %>% sum

# ms ------------------------------------------------------------------
# directory
setwd("/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/10_corredores_imoveis/ms")

# ms inside 45m -----
ms_in_45m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_inside_imoveis.shp")
ms_in_45m

ms_in_45m_group <- ms_in_45m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ms_in_45m_group$area_ha %>% sum
ms_in_45m_group$area_ha_r %>% sum


# ms outside 45m -----
ms_out_45m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_outside_imoveis.shp")
ms_out_45m

ms_out_45m_group <- ms_out_45m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ms_out_45m_group$area_ha %>% sum
ms_out_45m_group$area_ha_r %>% sum

# ms inside 250m -----
ms_in_250m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_inside_imoveis.shp")
ms_in_250m

ms_in_250m_group <- ms_in_250m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ms_in_250m_group$area_ha %>% sum
ms_in_250m_group$area_ha_r %>% sum

# ms outside 250m -----
ms_out_250m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_outside_imoveis.shp")
ms_out_250m

ms_out_250m_group <- ms_out_250m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ms_out_250m_group$area_ha %>% sum
ms_out_250m_group$area_ha_r %>% sum

# ms inside 500m -----
ms_in_500m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_inside_imoveis.shp")
ms_in_500m

ms_in_500m_group <- ms_in_500m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ms_in_500m_group$area_ha %>% sum
ms_in_500m_group$area_ha_r %>% sum

# ms outside 500m -----
ms_out_500m <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_outside_imoveis.shp")
ms_out_500m

ms_out_500m_group <- ms_out_500m %>% 
  dplyr::mutate(area_ha_r = as.numeric(round(sf::st_area(.)/1e4, 2))) %>% 
  sf::st_drop_geometry() %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha),
                   area_ha_r = sum(area_ha_r))
ms_out_500m_group$area_ha %>% sum
ms_out_500m_group$area_ha_r %>% sum

# analysis ----------------------------------------------------------------
analysis <- tibble::tibble(
  local = rep(c("BAMGES", "MA", "MS"), each = 6),
  suzano = rep(c("Dentro", "Fora"), 9),
  buffer = rep(c("90m", "500m", "1000m"), each = 2, len = 18),
  numero_frag = c(nrow(bamges_in_45m_group), nrow(bamges_out_45m_group),
                  nrow(bamges_in_250m_group), nrow(bamges_out_250m_group),
                  nrow(bamges_in_500m_group), nrow(bamges_out_500m_group),
                  nrow(ma_in_45m_group), nrow(ma_out_45m_group),
                  nrow(ma_in_250m_group), nrow(ma_out_250m_group),
                  nrow(ma_in_500m_group), nrow(ma_out_500m_group),
                  nrow(ms_in_45m_group), nrow(ms_out_45m_group),
                  nrow(ms_in_250m_group), nrow(ms_out_250m_group),
                  nrow(ms_in_500m_group), nrow(ms_out_500m_group)),
  area_ha = c(sum(bamges_in_45m_group$area_ha),
              sum(bamges_out_45m_group$area_ha),
              sum(bamges_in_250m_group$area_ha),
              sum(bamges_out_250m_group$area_ha),
              sum(bamges_in_500m_group$area_ha),
              sum(bamges_out_500m_group$area_ha),
              sum(ma_in_45m_group$area_ha),
              sum(ma_out_45m_group$area_ha),
              sum(ma_in_250m_group$area_ha),
              sum(ma_out_250m_group$area_ha),
              sum(ma_in_500m_group$area_ha),
              sum(ma_out_500m_group$area_ha),
              sum(ms_in_45m_group$area_ha),
              sum(ms_out_45m_group$area_ha),
              sum(ms_in_250m_group$area_ha),
              sum(ms_out_250m_group$area_ha),
              sum(ms_in_500m_group$area_ha),
              sum(ms_out_500m_group$area_ha))
  )
analysis

readr::write_csv(analysis, "00_analysis_fragmentos_conectados_corredores_lscorridors.csv")

# end ---------------------------------------------------------------------