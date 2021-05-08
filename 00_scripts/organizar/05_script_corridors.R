#' ---
#' title: corridors
#' author: mauricio vancine
#' date: 2020-11-30
#' ---

# packages ----------------------------------------------------------------
library(tidyverse)
library(here)
library(sf)
library(raster)

# options
options(scipen = 1e5, warn = -1)

# import data -------------------------------------------------------------
## bangem
# raster corridors
corr_raster_bamges <- raster::stack(dir(here::here("07_corridors", "bamges", "corridor_90m"), pattern = ".tif", full.names = TRUE))
corr_raster_bamges <- corr_raster_bamges[[-1]]
corr_raster_bamges
names(corr_raster_bamges)

# vector corridors
corr_vector_bamges <- purrr::map(dir(here::here("07_corridors", "bamges", "corridors_vector"), pattern = ".shp", recursive = TRUE, full.names = TRUE), sf::st_read, quiet = TRUE)
names(corr_vector_bamges) <- sub(".shp", "", dir(here::here("07_corridors", "bamges", "corridors_vector"), pattern = ".shp"))
corr_vector_bamges[1:2]

# target
target_bamges <- sf::st_read(here::here("02_vector", "00_targets", "target_bamges.shp")) %>% 
  sf::st_transform(crs = sf::st_crs(corr_raster_bamges))
target_bamges

# map
plot(target_bamges$geometry, col = "gray", axes = TRUE)
plot(corr_raster_bamges[[1]], legend = FALSE, add = TRUE)
plot(corr_vector_bamges[[1]]$geom, col = "red", add = TRUE)

## ma
# raster corridors
corr_raster_ma <- raster::stack(dir(here::here("07_corridors", "ma", "corridor_90m"), pattern = ".tif", full.names = TRUE))
corr_raster_ma <- corr_raster_ma[[-1]]
corr_raster_ma
names(corr_raster_ma)

# vector corridors
corr_vector_ma <- purrr::map(dir(here::here("07_corridors", "ma", "corridors_vector"), pattern = ".shp", recursive = TRUE, full.names = TRUE), sf::st_read, quiet = TRUE)
names(corr_vector_ma) <- sub(".shp", "", dir(here::here("07_corridors", "ma", "corridors_vector"), pattern = ".shp"))
corr_vector_ma[1:2]

# target
target_ma <- sf::st_read(here::here("02_vector", "00_targets", "target_ma.shp")) %>% 
  sf::st_transform(crs = sf::st_crs(corr_raster_bamges))
target_ma

# map
plot(target_ma$geometry, col = "gray", axes = TRUE)
plot(corr_raster_ma[[1]], legend = FALSE, add = TRUE)
plot(corr_vector_ma[[1]]$geom, col = "red", add = TRUE)


## ms
# raster corridors
corr_raster_ms <- raster::stack(dir(here::here("07_corridors", "ms", "corridor_90m"), pattern = ".tif", full.names = TRUE))
corr_raster_ms <- corr_raster_ms[[-1]]
names(corr_raster_ms) <- sub("_mapbiomas_2019_30m_rec_suzano_forest_wei_ms_90m", "_ms", names(corr_raster_ms))
corr_raster_ms

# vector corridors
corr_vector_ms <- purrr::map(dir(here::here("07_corridors", "ms", "corridors_vector"), pattern = ".shp", recursive = TRUE, full.names = TRUE), sf::st_read, quiet = TRUE)
names(corr_vector_ms) <- sub(".shp", "", dir(here::here("07_corridors", "ms", "corridors_vector"), pattern = ".shp"))
corr_vector_ms[1:2]

# target
target_ms <- sf::st_read(here::here("02_vector", "00_targets", "target_ms.shp")) %>% 
  sf::st_transform(crs = sf::st_crs(corr_raster_ms))
target_ms

# map
plot(target_ms$geometry, col = "gray", axes = TRUE)
plot(corr_raster_ma[[1]], legend = FALSE, add = TRUE)
plot(corr_vector_ma[[1]]$geom, col = "red", add = TRUE)



# extract values ----------------------------------------------------------
## bamges
# table
table_bamges <- list()

# bamges
for(i in 1:length(names(corr_raster_bamges))){
  
  # information
  print(names(corr_raster_bamges)[[i]])
  
  # select raster
  corr_raster_bamges_i <- corr_raster_bamges[[i]]
  
  # select vectors
  corr_vector_bamges_i <- corr_vector_bamges[grep(names(corr_raster_bamges_i), names(corr_vector_bamges))]
  
  # extract values
  for(j in 1:length(names(corr_vector_bamges_i))){
    
    # information
    print(names(corr_vector_bamges_)[[j]])
    
    # select vector
    corr_vector_bamges_i_j <- sf::st_transform(corr_vector_bamges_i[[j]], crs = sf::st_crs(corr_raster_bamges_i)) %>% 
      dplyr::summarise(dist = sum(dist))
    
    # erase
    # corr_vector_bamges_i_j_erase <- sf::st_difference(corr_vector_bamges_i_j, sf::st_combine(target_bamges))
    
    # length
    # corr_vector_bamges_i_j_erase$dist_erase <- sf::st_length(corr_vector_bamges_i_j_erase)
    
    # extract values
    corr_vector_bamges_i_j$freq <- raster::extract(corr_raster_bamges_i, corr_vector_bamges_i_j, fun = sum, na.rm = TRUE)
    
    # export
    sf::st_write(corr_vector_bamges_i_j, here::here("07_corridors", "bamges", "corridor_vector_proj_freq", paste0(names(corr_vector_bamges_i)[[j]], "_proj_freq.shp")), quiet = TRUE)
    # sf::st_write(corr_vector_bamges_i_j_erase, here::here("07_corridors", "bamges", "corridor_vector_proj_erase_length_freq", paste0(names(corr_vector_bamges_i)[[j]], "_proj_erase_length_freq.shp")))
    
    table_bamges <- rbind(table_bamges, data.frame(corridors = names(corr_vector_bamges_i)[[j]], length = corr_vector_bamges_i_j$dist, freq = corr_vector_bamges_i_j$freq))
  
    }
  
}

readr::write_csv(table_bamges, here::here("07_corridors", "bamges", "corridor_vector_proj_freq", "corridors_freq.csv"))


## ma
# table
table_ma <- list()

# ma
for(i in 1:length(names(corr_raster_ma))){
  
  # information
  print(names(corr_raster_ma)[[i]])
  
  # select raster
  corr_raster_ma_i <- corr_raster_ma[[i]]
  
  # select vectors
  corr_vector_ma_i <- corr_vector_ma[grep(names(corr_raster_ma_i), names(corr_vector_ma))]
  
  # extract values
  for(j in 1:length(names(corr_vector_ma_i))){
    
    # information
    print(names(corr_vector_ma_i)[[j]])
    
    # select vector
    corr_vector_ma_i_j <- sf::st_transform(corr_vector_ma_i[[j]], crs = sf::st_crs(corr_raster_ma_i)) %>% 
      dplyr::summarise(dist = sum(dist))
    
    # erase
    # corr_vector_ma_i_j_erase <- sf::st_difference(corr_vector_ma_i_j, sf::st_combine(target_ma))
    
    # length
    # corr_vector_ma_i_j_erase$dist_erase <- sf::st_length(corr_vector_ma_i_j_erase)
    
    # extract values
    corr_vector_ma_i_j$freq <- raster::extract(corr_raster_ma_i, corr_vector_ma_i_j, fun = sum, na.rm = TRUE)
    
    # export
    sf::st_write(corr_vector_ma_i_j, here::here("07_corridors", "ma", "corridor_vector_proj_freq", paste0(names(corr_vector_ma_i)[[j]], "_proj_freq.shp")), quiet = TRUE)
    # sf::st_write(corr_vector_ma_i_j_erase, here::here("07_corridors", "ma", "corridor_vector_proj_erase_length_freq", paste0(names(corr_vector_ma_i)[[j]], "_proj_erase_length_freq.shp")))
    
    table_ma <- rbind(table_ma, data.frame(corridors = names(corr_vector_ma_i)[[j]], length = corr_vector_ma_i_j$dist, freq = corr_vector_ma_i_j$freq))
    
  }
  
}

readr::write_csv(table_ma, here::here("07_corridors", "ma", "corridor_vector_proj_freq", "corridors_freq.csv"))




## ms
# table
table_ms <- list()

# ms
for(i in 1:length(names(corr_raster_ms))){
  
  # information
  print(names(corr_raster_ms)[[i]])
  
  # select raster
  corr_raster_ms_i <- corr_raster_ms[[i]]
  
  # select vectors
  corr_vector_ms_i <- corr_vector_ms[grep(names(corr_raster_ms_i), names(corr_vector_ms))]
  
  # extract values
  for(j in 1:length(names(corr_vector_ms_i))){
    
    # information
    print(names(corr_vector_ms_i)[[j]])
    
    # select vector
    corr_vector_ms_i_j <- sf::st_transform(corr_vector_ms_i[[j]], crs = sf::st_crs(corr_raster_ms_i)) %>% 
      dplyr::summarise(dist = sum(dist))
    
    # erase
    # corr_vector_ms_i_j_erase <- sf::st_difference(corr_vector_ms_i_j, sf::st_combine(target_ms))
    
    # length
    # corr_vector_ms_i_j_erase$dist_erase <- sf::st_length(corr_vector_ms_i_j_erase)
    
    # extract values
    corr_vector_ms_i_j$freq <- raster::extract(corr_raster_ms_i, corr_vector_ms_i_j, fun = sum, na.rm = TRUE)
    
    # export
    sf::st_write(corr_vector_ms_i_j, here::here("07_corridors", "ms", "corridor_vector_proj_freq", paste0(names(corr_vector_ms_i)[[j]], "_proj_freq.shp")), quiet = TRUE)
    # sf::st_write(corr_vector_ms_i_j_erase, here::here("07_corridors", "ms", "corridor_vector_proj_erase_length_freq", paste0(names(corr_vector_ms_i)[[j]], "_proj_erase_length_freq.shp")))
    
    table_ms <- rbind(table_ms, data.frame(corridors = names(corr_vector_ms_i)[[j]], length = corr_vector_ms_i_j$dist, freq = corr_vector_ms_i_j$freq))
    
  }
  
}

readr::write_csv(table_ms, here::here("07_corridors", "ms", "corridor_vector_proj_freq", "corridors_freq.csv"))

# end ---------------------------------------------------------------------
