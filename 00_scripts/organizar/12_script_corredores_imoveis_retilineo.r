#' ---
#' title: corredores fragmentos e imoveis
#' author: mauricio vancine
#' date: 2020-12-09
#' ---

# packages
library(sf)
library(tidyverse)

# directory
setwd("/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/10_corredores_imoveis/retilineo")

# bamges ------------------------------------------------------------------
# bamges inside -----
bamges_in <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_inside_imoveis.shp")
bamges_in

bamges_in_group <- bamges_in %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha))
bamges_in_group

sf::st_write(bamges_in_group, "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_inside_imoveis_group.shp")

# bamges outside ----
bamges_out <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_outside_imoveis.shp")
bamges_out

bamges_out_group <- bamges_out %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha))
bamges_out_group

sf::st_write(bamges_out_group, "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_outside_imoveis_group.shp")

# ma ------------------------------------------------------------------
# ma inside -----
ma_in <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_inside_imoveis.shp")
ma_in

ma_in_group <- ma_in %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha))
ma_in_group

sf::st_write(ma_in_group, "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_inside_imoveis_group.shp")

# ma outside ----
ma_out <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_outside_imoveis.shp")
ma_out

ma_out_group <- ma_out %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha))
ma_out_group

sf::st_write(ma_out_group, "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_outside_imoveis_group.shp")



# ms ------------------------------------------------------------------
# ms inside -----
ms_in <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_inside_imoveis.shp")
ms_in

ms_in_group <- ms_in %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha))
ms_in_group

sf::st_write(ms_in_group, "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_inside_imoveis_group.shp")

# ms outside ----
ms_out <- sf::st_read("mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_outside_imoveis.shp")
ms_out

ms_out_group <- ms_out %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(n = n(),
                   area_ha = sum(area_ha))
ms_out_group

sf::st_write(ms_out_group, "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_outside_imoveis_group.shp")


# analysis ----------------------------------------------------------------
analysis <- tibble::tibble(
  local = c("BAMGES", "BAMGES", "MA", "MA", "MS", "MS"),
  suzano = c("Dentro", "Fora", "Dentro", "Fora", "Dentro", "Fora"),
  numero_frag = c(nrow(bamges_in_group), nrow(bamges_out_group),
                  nrow(ma_in_group), nrow(ma_out_group),
                  nrow(ms_in_group), nrow(ms_out_group)),
  area_ha = c(sum(bamges_in_group$area_ha),
              sum(bamges_out_group$area_ha),
              sum(ma_in_group$area_ha),
              sum(ma_out_group$area_ha),
              sum(ms_in_group$area_ha),
              sum(ms_out_group$area_ha))
)
analysis

readr::write_csv(analysis, "00_analysis_fragmentos_conectados_corredores_retilineos.csv")

# end ---------------------------------------------------------------------