#' -----
#' objetivos: rppn
#' autor: mauricio vancine
#' data: 2020-11-14
#' -----

# iniciar o python
python3

# importar bibliotecas
import os
import grass.script as gs

# bamges ------------------------------------------------------------------------- #
dir_a = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/06_rppn"
os.chdir(dir_a)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_bamges_mask", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_bamges_mask")

gs.run_command("r.category", map = "suzano_forest_30m_erosion120m_null_clump_area_ha_bamges")

# null
ex = "suzano_forest_30m_null_bamges = if(suzano_forest_30m == 0, null(), suzano_forest_30m)"
gs.mapcalc(ex, overwrite = True)

# dilation
gs.run_command("r.neighbors", input = "suzano_forest_30m_null_bamges", output = "suzano_forest_30m_null_dilation30m_bamges", \
    method = "max", overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "suzano_forest_30m_null_dilation30m_bamges", \
    output = "suzano_forest_30m_null_dilation30m_clump_bamges", overwrite = True)

# adj
ex = "suzano_forest_30m_null_dilation30m_clump_adj_bamges = suzano_forest_30m_null_dilation30m_clump_bamges * suzano_forest_30m_null_bamges"
gs.mapcalc(ex, overwrite = True)

# area
gs.run_command("r.area", input = "suzano_forest_30m_null_dilation30m_clump_adj_bamges", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_bamges", overwrite = True)

# area in hectares
ex = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_bamges = suzano_forest_30m_null_dilation30m_clump_adj_area_bamges * 0.09"
gs.mapcalc(ex, overwrite = True)

# vectorization
gs.run_command("r.to.vect", input = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_bamges", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_bamges", type = "area", column = "area", overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_bamges", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_bamges.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

gs.run_command("v.out.ogr", input = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_bamges", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_bamges.shp", format = "ESRI_Shapefile", overwrite = True)


# erosion
gs.run_command("r.neighbors", input = "suzano_forest_30m", output = "suzano_forest_30m_erosion120m_bamges", \
    size = 9, method = "min", overwrite = True)

# null
ex = "suzano_forest_30m_erosion120m_null_bamges = if(suzano_forest_30m_erosion120m_bamges == 1, suzano_forest_30m_erosion120m_bamges, null())"
gs.mapcalc(ex, overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "suzano_forest_30m_erosion120m_null_bamges", \
    output = "suzano_forest_30m_erosion120m_null_clump_bamges", overwrite = True)

# area
gs.run_command("r.area", input = "suzano_forest_30m_erosion120m_null_clump_bamges", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_bamges", overwrite = True)

# area in hectares
ex = "suzano_forest_30m_erosion120m_null_clump_area_ha_bamges = suzano_forest_30m_erosion120m_null_clump_area_bamges * 0.09"
gs.mapcalc(ex, overwrite = True)

# vectorization
gs.run_command("r.to.vect", input = "suzano_forest_30m_erosion120m_null_clump_area_ha_bamges", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_ha_bamges", type = "area", column = "area", overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "suzano_forest_30m_erosion120m_null_clump_area_ha_bamges", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_ha_bamges.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

gs.run_command("v.out.ogr", input = "suzano_forest_30m_erosion120m_null_clump_area_ha_bamges", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_ha_bamges.shp", format = "ESRI_Shapefile", overwrite = True)


# ma ------------------------------------------------------------------------- #
dir_a = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/06_rppn"
os.chdir(dir_a)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ma_mask", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_ma_mask")

# null
ex = "suzano_forest_30m_null_ma = if(suzano_forest_30m == 0, null(), suzano_forest_30m)"
gs.mapcalc(ex, overwrite = True)

# dilation
gs.run_command("r.neighbors", input = "suzano_forest_30m_null_ma", output = "suzano_forest_30m_null_dilation30m_ma", \
    method = "max", overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "suzano_forest_30m_null_dilation30m_ma", \
    output = "suzano_forest_30m_null_dilation30m_clump_ma", overwrite = True)

# adj
ex = "suzano_forest_30m_null_dilation30m_clump_adj_ma = suzano_forest_30m_null_dilation30m_clump_ma * suzano_forest_30m_null_ma"
gs.mapcalc(ex, overwrite = True)

# area
gs.run_command("r.area", input = "suzano_forest_30m_null_dilation30m_clump_adj_ma", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_ma", overwrite = True)

# area in hectares
ex = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ma = suzano_forest_30m_null_dilation30m_clump_adj_area_ma * 0.09"
gs.mapcalc(ex, overwrite = True)

# vectorization
gs.run_command("r.to.vect", input = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ma", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ma", type = "area", column = "area", overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ma", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ma.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

gs.run_command("v.out.ogr", input = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ma", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ma.shp", format = "ESRI_Shapefile", overwrite = True)


# erosion
gs.run_command("r.neighbors", input = "suzano_forest_30m", output = "suzano_forest_30m_erosion120m_ma", \
    size = 9, method = "min", overwrite = True)

# null
ex = "suzano_forest_30m_erosion120m_null_ma = if(suzano_forest_30m_erosion120m_ma == 1, suzano_forest_30m_erosion120m_ma, null())"
gs.mapcalc(ex, overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "suzano_forest_30m_erosion120m_null_ma", \
    output = "suzano_forest_30m_erosion120m_null_clump_ma", overwrite = True)

# area
gs.run_command("r.area", input = "suzano_forest_30m_erosion120m_null_clump_ma", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_ma", overwrite = True)

# area in hectares
ex = "suzano_forest_30m_erosion120m_null_clump_area_ha_ma = suzano_forest_30m_erosion120m_null_clump_area_ma * 0.09"
gs.mapcalc(ex, overwrite = True)

# vectorization
gs.run_command("r.to.vect", input = "suzano_forest_30m_erosion120m_null_clump_area_ha_ma", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_ha_ma", type = "area", column = "area", overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "suzano_forest_30m_erosion120m_null_clump_area_ha_ma", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_ha_ma.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

gs.run_command("v.out.ogr", input = "suzano_forest_30m_erosion120m_null_clump_area_ha_ma", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_ha_ma.shp", format = "ESRI_Shapefile", overwrite = True)


# ms ------------------------------------------------------------------------- #
dir_a = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/06_rppn"
os.chdir(dir_a)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ms_mask", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_ms_mask")

# null
ex = "suzano_forest_30m_null_ms = if(suzano_forest_30m == 0, null(), suzano_forest_30m)"
gs.mapcalc(ex, overwrite = True)

# dilation
gs.run_command("r.neighbors", input = "suzano_forest_30m_null_ms", output = "suzano_forest_30m_null_dilation30m_ms", \
    method = "max", overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "suzano_forest_30m_null_dilation30m_ms", \
    output = "suzano_forest_30m_null_dilation30m_clump_ms", overwrite = True)

# adj
ex = "suzano_forest_30m_null_dilation30m_clump_adj_ms = suzano_forest_30m_null_dilation30m_clump_ms * suzano_forest_30m_null_ms"
gs.mapcalc(ex, overwrite = True)

# area
gs.run_command("r.area", input = "suzano_forest_30m_null_dilation30m_clump_adj_ms", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_ms", overwrite = True)

# area in hectares
ex = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ms = suzano_forest_30m_null_dilation30m_clump_adj_area_ms * 0.09"
gs.mapcalc(ex, overwrite = True)

# vectorization
gs.run_command("r.to.vect", input = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ms", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ms", type = "area", column = "area", overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ms", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ms.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

gs.run_command("v.out.ogr", input = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ms", \
    output = "suzano_forest_30m_null_dilation30m_clump_adj_area_ha_ms.shp", format = "ESRI_Shapefile", overwrite = True)


# erosion
gs.run_command("r.neighbors", input = "suzano_forest_30m", output = "suzano_forest_30m_erosion120m_ms", \
    size = 9, method = "min", overwrite = True)

# null
ex = "suzano_forest_30m_erosion120m_null_ms = if(suzano_forest_30m_erosion120m_ms == 1, suzano_forest_30m_erosion120m_ms, null())"
gs.mapcalc(ex, overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "suzano_forest_30m_erosion120m_null_ms", \
    output = "suzano_forest_30m_erosion120m_null_clump_ms", overwrite = True)

# area
gs.run_command("r.area", input = "suzano_forest_30m_erosion120m_null_clump_ms", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_ms", overwrite = True)

# area in hectares
ex = "suzano_forest_30m_erosion120m_null_clump_area_ha_ms = suzano_forest_30m_erosion120m_null_clump_area_ms * 0.09"
gs.mapcalc(ex, overwrite = True)

# vectorization
gs.run_command("r.to.vect", input = "suzano_forest_30m_erosion120m_null_clump_area_ha_ms", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_ha_ms", type = "area", column = "area", overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "suzano_forest_30m_erosion120m_null_clump_area_ha_ms", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_ha_ms.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

gs.run_command("v.out.ogr", input = "suzano_forest_30m_erosion120m_null_clump_area_ha_ms", \
    output = "suzano_forest_30m_erosion120m_null_clump_area_ha_ms.shp", format = "ESRI_Shapefile", overwrite = True)


# end -------------------------------------------------------------------------- #