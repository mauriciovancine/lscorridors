#' ---
#' title: corridors final
#' author: mauricio vancine
#' date: 2020-12-01
#' ---

# packages ----------------------------------------------------------------
library(tidyverse)
library(here)
library(sf)
library(raster)

# options
options(scipen = 1e5, warn = -1)

# bamges ------------------------------------------------------------------
# table
table_bamges <- readr::read_csv(here::here("06_corridors_lscorridos", "bamges", "corridor_vector_proj_freq", "corridors_freq.csv")) %>% 
  dplyr::mutate(targets = stringr::str_sub(corridors, end = -5), .before = 1) %>% 
  dplyr::mutate(freq_length = freq/length)
table_bamges

table_bamges_freq_max <- table_bamges %>% 
  dplyr::group_by(targets) %>% 
  dplyr::filter(freq == max(freq))
table_bamges_freq_max

table_bamges_length_min <- table_bamges %>% 
  dplyr::group_by(targets) %>% 
  dplyr::filter(length == min(length)) %>% 
  dplyr::distinct(targets, .keep_all = TRUE)
table_bamges_length_min

table_bamges_freq_length_max <- table_bamges %>% 
  dplyr::group_by(targets) %>% 
  dplyr::filter(freq_length == max(freq_length))
table_bamges_freq_length_max

# verify
table_bamges_freq_max$corridors
table_bamges_length_min$corridors
table_bamges_freq_length_max$corridors

# list bamges corridors
list_corr <- dir(here::here("06_corridors_lscorridos", "bamges", "corridor_vector_proj_freq"), 
                 pattern = ".shp", full.names = TRUE)
list_corr

## select freq max ----
list_corr_bamges_freq_max <- grep(paste0(table_bamges_freq_max$corridors, collapse = "|"), 
                                  list_corr, value = TRUE)
list_corr_bamges_freq_max

# import
corr_bamges_freq_max <- purrr::map(list_corr_bamges_freq_max, sf::st_read, quiet = TRUE)
corr_bamges_freq_max

# export
for(i in 1:length(corr_bamges_freq_max)){
  
  sf::st_write(corr_bamges_freq_max[[i]],
               here::here("06_corridors_lscorridos", "bamges", "corridor_vector_union", 
                          paste0(table_bamges_freq_max$corridors[i], "_freq_max.shp")),
               delete_layer = TRUE)
  
}

## select length min ----
list_corr_bamges_length_min <- grep(paste0(table_bamges_length_min$corridors, collapse = "|"), 
                                  list_corr, value = TRUE)
list_corr_bamges_length_min

# import
corr_bamges_length_min <- purrr::map(list_corr_bamges_length_min, sf::st_read, quiet = TRUE)
corr_bamges_length_min

# export
for(i in 1:length(corr_bamges_length_min)){
  
  sf::st_write(corr_bamges_length_min[[i]],
               here::here("06_corridors_lscorridos", "bamges", "corridor_vector_union", 
                          paste0(table_bamges_length_min$corridors[i], "_length_min.shp")),
               delete_layer = TRUE)
  
}

## select freq length max ----
list_corr_bamges_freq_length_max <- grep(paste0(table_bamges_freq_length_max$corridors, collapse = "|"), 
                                         list_corr, value = TRUE)
list_corr_bamges_freq_length_max

# import
corr_bamges_freq_length_max <- purrr::map(list_corr_bamges_freq_length_max, sf::st_read, quiet = TRUE)
corr_bamges_freq_length_max

# export
for(i in 1:length(corr_bamges_freq_length_max)){
  
  sf::st_write(corr_bamges_freq_length_max[[i]], 
               here::here("06_corridors_lscorridos", "bamges", "corridor_vector_union", 
                          paste0(table_bamges_freq_length_max$corridors[i], "_freq_length_max.shp")),
               delete_layer = TRUE)
  
}


# ma ------------------------------------------------------------------
# table
table_ma <- readr::read_csv(here::here("06_corridors_lscorridos", "ma", "corridor_vector_proj_freq", "corridors_freq.csv")) %>% 
  dplyr::mutate(targets = stringr::str_sub(corridors, end = -5), .before = 1) %>% 
  dplyr::mutate(freq_length = freq/length)
table_ma

table_ma_freq_max <- table_ma %>% 
  dplyr::group_by(targets) %>% 
  dplyr::filter(freq == max(freq)) 
table_ma_freq_max

table_ma_length_min <- table_ma %>% 
  dplyr::group_by(targets) %>% 
  dplyr::filter(length == min(length))
table_ma_length_min

table_ma_freq_length_max <- table_ma %>% 
  dplyr::group_by(targets) %>% 
  dplyr::filter(freq_length == max(freq_length))
table_ma_freq_length_max

# verify
table_ma_freq_max$corridors
table_ma_length_min$corridors
table_ma_freq_length_max$corridors

# list ma corridors
list_corr <- dir(here::here("06_corridors_lscorridos", "ma", "corridor_vector_proj_freq"), 
                 pattern = ".shp", full.names = TRUE)
list_corr

## select freq max ----
list_corr_ma_freq_max <- grep(paste0(table_ma_freq_max$corridors, collapse = "|"), 
                              list_corr, value = TRUE)
list_corr_ma_freq_max

# import
corr_ma_freq_max <- purrr::map(list_corr_ma_freq_max, sf::st_read, quiet = TRUE)
corr_ma_freq_max

# export
for(i in 1:length(corr_ma_freq_max)){
  
  sf::st_write(corr_ma_freq_max[[i]],
               here::here("06_corridors_lscorridos", "ma", "corridor_vector_union", 
                          paste0(table_ma_freq_max$corridors[i], "_freq_max.shp")))
  
}

## select length min ----
list_corr_ma_length_min <- grep(paste0(table_ma_length_min$corridors, collapse = "|"), 
                                list_corr, value = TRUE)
list_corr_ma_length_min

# import
corr_ma_length_min <- purrr::map(list_corr_ma_length_min, sf::st_read, quiet = TRUE)
corr_ma_length_min

# export
for(i in 1:length(corr_ma_length_min)){
  
  sf::st_write(corr_ma_length_min[[i]],
               here::here("06_corridors_lscorridos", "ma", "corridor_vector_union", 
                          paste0(table_ma_length_min$corridors[i], "_length_min.shp")))
  
}

## select freq length max ----
list_corr_ma_freq_length_max <- grep(paste0(table_ma_freq_length_max$corridors, collapse = "|"), 
                                     list_corr, value = TRUE)
list_corr_ma_freq_length_max

# import
corr_ma_freq_length_max <- purrr::map(list_corr_ma_freq_length_max, sf::st_read, quiet = TRUE)
corr_ma_freq_length_max

# export
for(i in 1:length(corr_ma_freq_length_max)){
  
  sf::st_write(corr_ma_freq_length_max[[i]], 
               here::here("06_corridors_lscorridos", "ma", "corridor_vector_union", 
                          paste0(table_ma_freq_length_max$corridors[i], "_freq_length_max.shp")))
  
}


# ms ------------------------------------------------------------------
# table
table_ms <- readr::read_csv(here::here("06_corridors_lscorridos", "ms", "corridor_vector_proj_freq", "corridors_freq.csv")) %>% 
  dplyr::mutate(targets = stringr::str_sub(corridors, end = -5), .before = 1) %>% 
  dplyr::mutate(freq_length = freq/length)
table_ms

table_ms_freq_max <- table_ms %>% 
  dplyr::group_by(targets) %>% 
  dplyr::filter(freq == max(freq)) %>% 
  dplyr::distinct(targets, .keep_all = TRUE)
table_ms_freq_max

table_ms_length_min <- table_ms %>% 
  dplyr::group_by(targets) %>% 
  dplyr::filter(length == min(length)) %>% 
  dplyr::distinct(targets, .keep_all = TRUE)
table_ms_length_min

table_ms_freq_length_max <- table_ms %>% 
  dplyr::group_by(targets) %>% 
  dplyr::filter(freq_length == max(freq_length))
table_ms_freq_length_max

# verify
table_ms_freq_max$corridors
table_ms_length_min$corridors
table_ms_freq_length_max$corridors

# list ms corridors
list_corr <- dir(here::here("06_corridors_lscorridos", "ms", "corridor_vector_proj_freq"), 
                 pattern = ".shp", full.names = TRUE)
list_corr

## select freq max ----
list_corr_ms_freq_max <- grep(paste0(table_ms_freq_max$corridors, collapse = "|"), 
                              list_corr, value = TRUE)
list_corr_ms_freq_max

# import
corr_ms_freq_max <- purrr::map(list_corr_ms_freq_max, sf::st_read, quiet = TRUE)
corr_ms_freq_max

# export
for(i in 1:length(corr_ms_freq_max)){
  
  sf::st_write(corr_ms_freq_max[[i]],
               here::here("06_corridors_lscorridos", "ms", "corridor_vector_union", 
                          paste0(table_ms_freq_max$corridors[i], "_freq_max.shp")))
  
}

## select length min ----
list_corr_ms_length_min <- grep(paste0(table_ms_length_min$corridors, collapse = "|"), 
                                list_corr, value = TRUE)
list_corr_ms_length_min

# import
corr_ms_length_min <- purrr::map(list_corr_ms_length_min, sf::st_read, quiet = TRUE)
corr_ms_length_min

# export
for(i in 1:length(corr_ms_length_min)){
  
  sf::st_write(corr_ms_length_min[[i]],
               here::here("06_corridors_lscorridos", "ms", "corridor_vector_union", 
                          paste0(table_ms_length_min$corridors[i], "_length_min.shp")))
  
}

## select freq_length_max ----
list_corr_ms_freq_length_max <- grep(paste0(table_ms_freq_length_max$corridors, collapse = "|"), 
                                     list_corr, value = TRUE)
list_corr_ms_freq_length_max

# import
corr_ms_freq_length_max <- purrr::map(list_corr_ms_freq_length_max, sf::st_read, quiet = TRUE)
corr_ms_freq_length_max

# export
for(i in 1:length(corr_ms_freq_length_max)){
  
  sf::st_write(corr_ms_freq_length_max[[i]], 
               here::here("06_corridors_lscorridos", "ms", "corridor_vector_union", 
                          paste0(table_ms_freq_length_max$corridors[i], "_freq_length_max.shp")))
  
}


# end ---------------------------------------------------------------------