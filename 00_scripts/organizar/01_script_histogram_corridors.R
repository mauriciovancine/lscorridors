#' ---
#' title: histograms of structural connectivity
#' author: mauricio vancine
#' date: 2020-10-19
#' ---

# packages ----------------------------------------------------------------
library(tidyverse)
library(here)
library(scales)
library(sf)

# options
options(scipen = 1e5)

# import data -------------------------------------------------------------
# fragments
frag <- purrr::map(dir(here::here("05_area", "fragmentos"), pattern = ".shp", full.names = TRUE), sf::st_read)
frag

names <- c("BAMGES", "MA", "MS", "SP1", "SP2")
names

# histograms --------------------------------------------------------------
# hist
for(i in 1:length(frag)){
  print(i)
  frag[[i]] %>% 
    sf::st_drop_geometry() %>% 
    ggplot() +
    aes(x = log10(area_ha + 1)) +
    geom_histogram(fill = "steelblue", 
                   col = "white", breaks = c(0, 1, 2, 3, 4, 5, 6)) +
    stat_bin(aes(y = ..count.., label = paste0(round(..count../sum(..count..), 4)*100, "%")),
             geom = "text", size = 5, 
             breaks = c(0, 1, 2, 3, 4, 5, 6),
             vjust = -.5, hjust = .4) +
    scale_x_continuous(breaks = c(0, 1, 2, 3, 4, 5, 6),
                  labels = c(0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6)) +
    theme_classic() +
    labs(title = names[[i]], x = "Área dos fragmentos (log10(ha))", y = "Frequência") +
    theme(title = element_text(size = 20),
          axis.title = element_text(size = 18),
          axis.text = element_text(size = 15),
          axis.text.y = element_text(angle = 90, hjust = .5)) +
    ggsave(here::here("05_area", "fragmentos", paste0("hist_", names[[i]], ".png")), 
           wi = 20, he = 15, un = "cm", dpi = 300)
}


# draft -------------------------------------------------------------------
# com corredor
da_cc %>% 
  ggplot() +
  aes(x = X3) +
  geom_histogram(fill = "steelblue", 
                 col = "white", breaks = c(1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9)) +
  stat_bin(aes(y = ..count.., label = paste0(round(..count../sum(..count..), 4)*100, "%")),
           geom = "text", size = 5, 
           breaks = c(1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9),
           vjust = -.5, hjust = .4) +
  scale_x_log10(breaks = trans_breaks("log10", function(x) {10^x}),
                labels = trans_format("log10", math_format(10^.x))) +
  theme_classic() +
  labs(title = "Com corredor", x = "Área dos fragmentos (log10(ha))", y = "Frequência") +
  theme(title = element_text(size = 20),
        axis.title = element_text(size = 18),
        axis.text = element_text(size = 15),
        axis.text.y = element_text(angle = 90, hjust = .5))


# area e número de manchas
da %>% 
  ggplot() + 
  aes(x = corredor, y = X3) +
  geom_boxplot(color = c("#440154", "#FFCB00"), fill = "steelblue") +
  scale_y_log10(breaks = trans_breaks("log10", function(x) {10^x}),
                labels = trans_format("log10", math_format(10^.x))) +
  theme_classic() +
  labs(x = "Corredor", y = "Área dos fragmentos (log10(ha))") +
  theme(axis.title = element_text(size = 18),
        axis.text = element_text(size = 15)) +
  annotate(geom = "text", x = 1, y = 5e9, label = paste0("n = ", nrow(da_sc)), size = 8) +
  annotate(geom = "text", x = 2, y = 5e9, label = paste0("n = ", nrow(da_cc)), size = 8)

