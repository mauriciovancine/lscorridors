#' ---
#' title: corridors final
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

# bamges ------------------------------------------------------------------
# list bamges corridors
list_corr_bamges <- dir(here::here("06_corridors_lscorridos", "bamges", "corridor_vector_union", "02_overlay_target_edit"), 
                 pattern = ".shp", full.names = TRUE)
list_corr_bamges

# import
corr_bamges <- purrr::map_dfr(list_corr_bamges, sf::st_read, quiet = TRUE) %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(dist = sum(a_dist),
                   freq = sum(a_freq)) %>% 
  dplyr::mutate(length = sf::st_length(.),
                length_km = sf::st_length(.)/1e3)
corr_bamges

plot(corr_bamges$geometry)

# export
sf::st_write(corr_bamges,
             here::here("06_corridors_lscorridos", "bamges", "corridor_vector_union", "03_overlay_target_edit_union", 
                        "corr_bamges.shp"))

# ma ------------------------------------------------------------------
# list ma corridors
list_corr_ma <- dir(here::here("06_corridors_lscorridos", "ma", "corridor_vector_union", "02_overlay_target_edit"), 
                    pattern = ".shp", full.names = TRUE)[10:22]
list_corr_ma

# import
corr_ma <- purrr::map_dfr(list_corr_ma, sf::st_read, quiet = TRUE) %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(dist = sum(a_dist),
                   freq = sum(a_freq)) %>% 
  dplyr::mutate(length = sf::st_length(.),
                length_km = sf::st_length(.)/1e3)
corr_ma

plot(corr_ma$geometry)

# export
sf::st_write(corr_ma,
             here::here("06_corridors_lscorridos", "ma", "corridor_vector_union", "03_overlay_target_edit_union", 
                        "corr_ma.shp"))


# ms ------------------------------------------------------------------
# list ms corridors
list_corr_ms <- dir(here::here("06_corridors_lscorridos", "ms", "corridor_vector_union", "02_overlay_target_edit"), 
                    pattern = ".shp", full.names = TRUE)
list_corr_ms

# import
corr_ms <- purrr::map_dfr(list_corr_ms, sf::st_read, quiet = TRUE) %>% 
  dplyr::group_by(a_cat) %>% 
  dplyr::summarise(dist = sum(a_dist),
                   freq = sum(a_freq)) %>% 
  dplyr::mutate(length = sf::st_length(.),
                length_km = sf::st_length(.)/1e3)
corr_ms

plot(corr_ms$geometry)

# export
sf::st_write(corr_ms,
             here::here("06_corridors_lscorridos", "ms", "corridor_vector_union", "03_overlay_target_edit_union", 
                        "corr_ms.shp"))
# end ---------------------------------------------------------------------