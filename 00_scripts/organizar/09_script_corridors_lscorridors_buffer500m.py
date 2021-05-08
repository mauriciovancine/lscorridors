#' -----
#' objetivos: corredores
#' autor: mauricio vancine
#' data: 2020-12-02
#' -----

# iniciar o python
python3

# importar bibliotecas
import os, glob
import grass.script as gs

# addons
# gs.run_command("g.extension", extension = "r.area", operation = "add")

# bamges ------------------------------------------------------------------------- #
# define region
gs.run_command("g.region", flags = "ap", vector = "unf_bamges_mask", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_bamges_mask")

# buffer bamges
gs.run_command("v.buffer", input = "corr_bamges", output = "corr_bamges_buffer500m", distance = 500, overwrite = True)    

# directory
dir_bamges = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corredores_buffer500m/bamges"
os.chdir(dir_bamges)

# select area vector overlap with corridor
gs.run_command("v.select", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha", \
    binput = "corr_bamges_buffer500m",
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m", \
    operator = "overlap", overwrite = True)

# export vector
gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "corr_bamges_buffer500m", \
    output = "corr_bamges_buffer500m.shp", \
    format = "ESRI_Shapefile", overwrite = True)



# corridor
gs.run_command("v.to.rast", \
    input = "corr_bamges_buffer500m", \
    output = "corr_bamges_buffer500m_30m_null", \
    use = "val", value = 1, overwrite = True)

gs.run_command("v.to.rast", \
    input = "corr_bamges_buffer500m", \
    output = "corr_bamges_buffer500m_30m", \
    use = "val", value = 1, overwrite = True)
gs.run_command("r.null", map = "corr_bamges_buffer500m_30m", null = 0, overwrite = True)

# add corridor to mapbiomas and suzano
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m = mapbiomas_2019_30m_rec_forest_suzano + corr_bamges_buffer500m_30m", overwrite = True)
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m_null = if(mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m > 0, 1, null())", overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m_null_clump_bamges", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m_null_clump_bamges", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m_null_area_bamges.csv", separator = "comma", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m_null_clump_bamges", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m_null_area_bamges", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m_null_area_bamges_ha = mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m_null_area_bamges * 0.09"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m_null_area_bamges_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_bamges_buffer500m_null_area_bamges_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)



# area inside corridor
# define region
gs.run_command("g.region", flags = "ap", raster = "corr_bamges_buffer500m_30m_null", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "corr_bamges_buffer500m_30m_null")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer500m_bamges_area.csv", separator = "comma", overwrite = True)

## area inside corridor and imoveis
# rasterize
gs.mapcalc("suzano_properties_30m_inside_bamges_buffer500m = suzano_properties_30m", overwrite = True)
gs.mapcalc("suzano_properties_30m_inside_bamges_bin_buffer500m = suzano_properties_30m_inside_bamges_buffer500m", overwrite = True)
gs.run_command("r.null", map = "suzano_properties_30m_inside_bamges_bin_buffer500m", null = 0)
gs.mapcalc("suzano_properties_30m_outside_bamges_buffer500m = if(suzano_properties_30m_inside_bamges_bin_buffer500m == 0, 1, null())", overwrite = True)

## area inside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_inside_bamges_buffer500m", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_inside_bamges_buffer500m")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer500m_bamges_inside_bamges_area.csv", separator = "comma", overwrite = True)


## area inside corridor and ouside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_outside_bamges_buffer500m", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_outside_bamges_buffer500m")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer500m_bamges_outside_bamges_area.csv", separator = "comma", overwrite = True)











# ma ------------------------------------------------------------------------- #
# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ma_mask", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_ma_mask")

# buffer ma
gs.run_command("v.buffer", input = "corr_ma", output = "corr_ma_buffer500m", distance = 500, overwrite = True)    

# directory
dir_ma = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corredores_buffer500m/ma"
os.chdir(dir_ma)

# select area vector overlap with corridor
gs.run_command("v.select", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha", \
    binput = "corr_ma_buffer500m", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m", \
    operator = "overlap", overwrite = True)

# export vector
gs.run_command("v.out.ogr", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", input = "corr_ma_buffer500m", \
    output = "corr_ma_buffer500m.shp", \
    format = "ESRI_Shapefile", overwrite = True)



# corridor
gs.run_command("v.to.rast", input = "corr_ma_buffer500m", \
    output = "corr_ma_buffer500m_30m_null", use = "val", value = 1, overwrite = True)

gs.run_command("v.to.rast", input = "corr_ma_buffer500m", \
    output = "corr_ma_buffer500m_30m", use = "val", value = 1, overwrite = True)
gs.run_command("r.null", map = "corr_ma_buffer500m_30m", null = 0, overwrite = True)

# add corridor to mapbiomas and suzano
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m = mapbiomas_2019_30m_rec_forest_suzano + corr_ma_buffer500m_30m", overwrite = True)
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m_null = if(mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m > 0, 1, null())", overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m_null_clump_ma", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m_null_clump_ma", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m_null_area_ma.csv", separator = "comma", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m_null_clump_ma", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m_null_area_ma", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m_null_area_ma_ha = mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m_null_area_ma * 0.09"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m_null_area_ma_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_ma_buffer500m_null_area_ma_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)



# area inside corridor
# define region
gs.run_command("g.region", flags = "ap", raster = "corr_ma_buffer500m_30m_null", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "corr_ma_buffer500m_30m_null")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer500m_ma_area.csv", separator = "comma", overwrite = True)

## area inside corridor and imoveis
# rasterize
gs.mapcalc("suzano_properties_30m_inside_ma_buffer500m = suzano_properties_30m", overwrite = True)
gs.mapcalc("suzano_properties_30m_inside_ma_bin_buffer500m = suzano_properties_30m_inside_ma_buffer500m", overwrite = True)
gs.run_command("r.null", map = "suzano_properties_30m_inside_ma_bin_buffer500m", null = 0)
gs.mapcalc("suzano_properties_30m_outside_ma_buffer500m = if(suzano_properties_30m_inside_ma_bin_buffer500m == 0, 1, null())", overwrite = True)

## area inside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_inside_ma_buffer500m", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_inside_ma_buffer500m")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer500m_ma_inside_ma_area.csv", separator = "comma", overwrite = True)


## area inside corridor and ouside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_outside_ma_buffer500m", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_outside_ma_buffer500m")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer500m_ma_outside_ma_area.csv", separator = "comma", overwrite = True)












# ms ------------------------------------------------------------------------- #
# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ms_mask", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_ms_mask")

# buffer ms
gs.run_command("v.buffer", input = "corr_ms", output = "corr_ms_buffer500m", distance = 500, overwrite = True)    

# directory
dir_ms = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corredores_buffer500m/ms"
os.chdir(dir_ms)

# select area vector overlap with corridor
gs.run_command("v.select", ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha", \
    binput = "corr_ms_buffer500m",
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m", \
    operator = "overlap", overwrite = True)

# export vector
gs.run_command("v.out.ogr", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", input = "corr_ms_buffer500m", \
    output = "corr_ms_buffer500m.shp", \
    format = "ESRI_Shapefile", overwrite = True)



# corridor
gs.run_command("v.to.rast", input = "corr_ms_buffer500m", \
    output = "corr_ms_buffer500m_30m_null", use = "val", value = 1, overwrite = True)

gs.run_command("v.to.rast", input = "corr_ms_buffer500m", \
    output = "corr_ms_buffer500m_30m", use = "val", value = 1, overwrite = True)
gs.run_command("r.null", map = "corr_ms_buffer500m_30m", null = 0, overwrite = True)

# add corridor to mapbiomas and suzano
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m = mapbiomas_2019_30m_rec_forest_suzano + corr_ms_buffer500m_30m", overwrite = True)
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m_null = if(mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m > 0, 1, null())", overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m_null_clump_ms", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m_null_clump_ms", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m_null_area_ms.csv", separator = "comma", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m_null_clump_ms", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m_null_area_ms", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m_null_area_ms_ha = mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m_null_area_ms * 0.09"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m_null_area_ms_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corr_ms_buffer500m_null_area_ms_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)



# area inside corridor
# define region
gs.run_command("g.region", flags = "ap", raster = "corr_ms_buffer500m_30m_null", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "corr_ms_buffer500m_30m_null")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer500m_ms_area.csv", separator = "comma", overwrite = True)

## area inside corridor and imoveis
# rasterize
gs.mapcalc("suzano_properties_30m_inside_ms_buffer500m = suzano_properties_30m", overwrite = True)
gs.mapcalc("suzano_properties_30m_inside_ms_bin_buffer500m = suzano_properties_30m_inside_ms_buffer500m", overwrite = True)
gs.run_command("r.null", map = "suzano_properties_30m_inside_ms_bin_buffer500m", null = 0)
gs.mapcalc("suzano_properties_30m_outside_ms_buffer500m = if(suzano_properties_30m_inside_ms_bin_buffer500m == 0, 1, null())", overwrite = True)

## area inside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_inside_ms_buffer500m", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_inside_ms_buffer500m")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer500m_ms_inside_ms_area.csv", separator = "comma", overwrite = True)


## area inside corridor and ouside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_outside_ms_buffer500m", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_outside_ms_buffer500m")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_buffer500m_ms_outside_ms_area.csv", separator = "comma", overwrite = True)


# end -------------------------------------------------------------------------- #