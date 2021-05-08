#' -----
#' objetivos: corredores
#' autor: mauricio vancine
#' data: 16-10-2020
#' -----

# iniciar o python
python3

# importar bibliotecas
import os
import grass.script as gs

# addons
# gs.run_command("g.extension", extension = "r.area", operation = "add")

# bamges ------------------------------------------------------------------------- #
dir_a = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/05_area"
os.chdir(dir_a)

# define region
gs.run_command("g.region", flags = "ap", vector = "bacia_nivel5_corredor_BAMGES", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", flags = "i", vector = "bacia_nivel5_corredor_BAMGES")

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_BAMGES", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_BAMGES", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES.csv", separator = "comma", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_BAMGES", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha = mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES * 0.09"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

# vectorize area
gs.run_command("r.to.vect", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha", type = "area", column = "area_ha", overwrite = True)

# select area vector overlap with corridor
gs.run_command("v.select", ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha", binput = "corredor_BAMGES_buffer",
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer", operator = "overlap", overwrite = True)

# export vector
gs.run_command("v.out.ogr", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer.shp", format = "ESRI_Shapefile", overwrite = True)



# corridor
gs.run_command("v.to.rast", input = "corredor_BAMGES_buffer", output = "corredor_BAMGES_buffer_30m_null", use = "val", value = 1, overwrite = True)

gs.run_command("v.to.rast", input = "corredor_BAMGES_buffer", output = "corredor_BAMGES_buffer_30m", use = "val", value = 1, overwrite = True)
gs.run_command("r.null", map = "corredor_BAMGES_buffer_30m", null = 0, overwrite = True)

# add corridor to mapbiomas and suzano
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer = mapbiomas_2019_30m_rec_forest_suzano + corredor_BAMGES_buffer_30m", overwrite = True)
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null = if(mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer > 0, 1, null())", overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_clump_BAMGES", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_clump_BAMGES", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES.csv", separator = "comma", overwrite = True)

gs.run_command("r.stats", flags = "al", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_clump_BAMGES", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES.txt", overwrite = True)

# replace space into equal
fi = open("mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES.txt", "r")
fi_da = fi.read()
fi.close()

fi_da_e = fi_da.replace("  ", "=")
fi_da_e_s = fi_da_e.split("*")

fi = open("mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES.txt", "w")
fi.write(fi_da_e_s[0])
fi.close()

# reclass
gs.run_command("r.reclass", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_clump_BAMGES", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES_m2", \
    rules = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES.txt", verbose = False, quiet = True, overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES_ha = mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES_m2 * 0.0001"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)




# area inside corridor
# define region
gs.run_command("g.region", flags = "ap", raster = "corredor_BAMGES_buffer_30m_null", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "corredor_BAMGES_buffer_30m_null")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_BAMGES_area.csv", separator = "comma", overwrite = True)



## area inside corridor and imoveis
# rasterize
gs.mapcalc("suzano_properties_30m_inside_BAMGES = suzano_properties_30m", overwrite = True)
gs.mapcalc("suzano_properties_30m_inside_BAMGES_bin = suzano_properties_30m_inside_BAMGES", overwrite = True)
gs.run_command("r.null", map = "suzano_properties_30m_inside_BAMGES_bin", null = 0)
gs.mapcalc("suzano_properties_30m_outside_BAMGES = if(suzano_properties_30m_inside_BAMGES_bin == 0, 1, null())", overwrite = True)

## area inside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_inside_BAMGES", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_inside_BAMGES")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_BAMGES_inside_BAMGES_area.csv", separator = "comma", overwrite = True)


## area inside corridor and ouside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_outside_BAMGES", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_outside_BAMGES")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_BAMGES_outside_BAMGES_area.csv", separator = "comma", overwrite = True)



# ma ------------------------------------------------------------------------- #
dir_a = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/05_area"
os.chdir(dir_a)

# define region
gs.run_command("g.region", flags = "ap", vector = "bacia_nivel5_corredor_MA", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "bacia_nivel5_corredor_MA")

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_MA", overwrite = True)

# export area by patch
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_MA", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA.csv", separator = "comma", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_MA", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha = mapbiomas_2019_30m_rec_forest_suzano_null_area_MA * 0.09"
gs.mapcalc(ex, overwrite = True)

# export raster
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

# vectorize area
gs.run_command("r.to.vect", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha", type = "area", column = "area_ha", overwrite = True)

# select area vector overlap with corridor
gs.run_command("v.select", ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha", binput = "corredor_MA_buffer",
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer", operator = "overlap", overwrite = True)

# export vector
gs.run_command("v.out.ogr", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer.shp", format = "ESRI_Shapefile", overwrite = True)





# corridor
gs.run_command("v.to.rast", input = "corredor_BAMGES_buffer", output = "corredor_BAMGES_buffer_30m_null", use = "val", value = 1, overwrite = True)

gs.run_command("v.to.rast", input = "corredor_BAMGES_buffer", output = "corredor_BAMGES_buffer_30m", use = "val", value = 1, overwrite = True)
gs.run_command("r.null", map = "corredor_BAMGES_buffer_30m", null = 0, overwrite = True)

# add corridor to mapbiomas and suzano
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer = mapbiomas_2019_30m_rec_forest_suzano + corredor_BAMGES_buffer_30m", overwrite = True)
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null = if(mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer > 0, 1, null())", overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_clump_BAMGES", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_clump_BAMGES", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_clump_BAMGES", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES.csv", separator = "comma", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES_ha = mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES * 0.09"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_BAMGES_buffer_null_area_BAMGES_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)



# area inside corridor
# define region
gs.run_command("g.region", flags = "ap", raster = "corredor_MA_buffer_30m_null", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "corredor_MA_buffer_30m_null")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_MA_area.csv", separator = "comma", overwrite = True)



## area inside corridor and imoveis
# rasterize
gs.mapcalc("suzano_properties_30m_inside_MA = suzano_properties_30m", overwrite = True)
gs.mapcalc("suzano_properties_30m_inside_MA_bin = suzano_properties_30m_inside_MA", overwrite = True)
gs.run_command("r.null", map = "suzano_properties_30m_inside_MA_bin", null = 0)
gs.mapcalc("suzano_properties_30m_outside_MA = if(suzano_properties_30m_inside_MA_bin == 0, 1, null())", overwrite = True)

## area inside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_inside_MA", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_inside_MA")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_MA_inside_area.csv", separator = "comma", overwrite = True)


## area inside corridor and ouside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_outside_suzano_properties", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_outside_MA")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_MA_outside_area.csv", separator = "comma", overwrite = True)




# ms ------------------------------------------------------------------------- #
dir_a = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/05_area"
os.chdir(dir_a)

# define region
gs.run_command("g.region", flags = "ap", vector = "bacia_nivel5_corredor_MS", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "bacia_nivel5_corredor_MS")

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_MS", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_MS", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS.csv", separator = "comma", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_MS", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha = mapbiomas_2019_30m_rec_forest_suzano_null_area_MS * 0.09"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

# vectorize area
gs.run_command("r.to.vect", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha", type = "area", column = "area_ha", overwrite = True)

# select area vector overlap with corridor
gs.run_command("v.select", ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha", binput = "corredor_MS_buffer",
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer", operator = "overlap", overwrite = True)

# export vector
gs.run_command("v.out.ogr", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer.shp", format = "ESRI_Shapefile", overwrite = True)



# corridor
gs.run_command("v.to.rast", input = "corredor_MS_buffer", output = "corredor_MS_buffer_30m_null", use = "val", value = 1, overwrite = True)

gs.run_command("v.to.rast", input = "corredor_MS_buffer", output = "corredor_MS_buffer_30m", use = "val", value = 1, overwrite = True)
gs.run_command("r.null", map = "corredor_MS_buffer_30m", null = 0, overwrite = True)

# add corridor to mapbiomas and suzano
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer = mapbiomas_2019_30m_rec_forest_suzano + corredor_MS_buffer_30m", overwrite = True)
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer_null = if(mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer > 0, 1, null())", overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer_null_clump_MS", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer_null_clump_MS", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer_null_area_MS", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer_null_clump_MS", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer_null_area_MS.csv", separator = "comma", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer_null_area_MS_ha = mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer_null_area_MS * 0.09"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer_null_area_MS_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_MS_buffer_null_area_MS_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)



# area inside corridor
# define region
gs.run_command("g.region", flags = "ap", raster = "corredor_MS_buffer_30m_null", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "corredor_MS_buffer_30m_null")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_MS_area.csv", separator = "comma", overwrite = True)



## area inside corridor and imoveis
# rasterize
gs.mapcalc("suzano_properties_30m_inside_MS = suzano_properties_30m", overwrite = True)
gs.mapcalc("suzano_properties_30m_inside_MS_bin = suzano_properties_30m_inside_MS", overwrite = True)
gs.run_command("r.null", map = "suzano_properties_30m_inside_MS_bin", null = 0)
gs.mapcalc("suzano_properties_30m_outside_MS = if(suzano_properties_30m_inside_MS_bin == 0, 1, null())", overwrite = True)

## area inside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_inside_MS", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_inside_MS")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_MS_inside_area.csv", separator = "comma", overwrite = True)


## area inside corridor and ouside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_outside_MS", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_outside_MS")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_MS_outside_area.csv", separator = "comma", overwrite = True)



# sp1 ------------------------------------------------------------------------- #
dir_a = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/05_area"
os.chdir(dir_a)

# define region
gs.run_command("g.region", flags = "ap", vector = "bacia_nivel5_corredor_SP1", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "bacia_nivel5_corredor_SP1")

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_SP1", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_SP1", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_SP1", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1.csv", separator = "comma", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1_ha = mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1 * 0.09"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

# vectorize area
gs.run_command("r.to.vect", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1_ha", type = "area", column = "area_ha", overwrite = True)

# select area vector overlap with corridor
gs.run_command("v.select", ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1_ha", binput = "corredor_SP1_buffer",
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1_ha_corredor_buffer", operator = "overlap", overwrite = True)

# export vector
gs.run_command("v.out.ogr", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1_ha_corredor_buffer", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP1_ha_corredor_buffer.shp", format = "ESRI_Shapefile", overwrite = True)



# corridor
gs.run_command("v.to.rast", input = "corredor_SP1_buffer", output = "corredor_SP1_buffer_30m_null", use = "val", value = 1, overwrite = True)

gs.run_command("v.to.rast", input = "corredor_SP1_buffer", output = "corredor_SP1_buffer_30m", use = "val", value = 1, overwrite = True)
gs.run_command("r.null", map = "corredor_SP1_buffer_30m", null = 0, overwrite = True)

# add corridor to mapbiomas and suzano
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer = mapbiomas_2019_30m_rec_forest_suzano + corredor_SP1_buffer_30m", overwrite = True)
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer_null = if(mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer > 0, 1, null())", overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer_null_clump_SP1", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer_null_clump_SP1", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer_null_area_SP1", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer_null_clump_SP1", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer_null_area_SP1.csv", separator = "comma", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer_null_area_SP1_ha = mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer_null_area_SP1 * 0.09"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer_null_area_SP1_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP1_buffer_null_area_SP1_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)



# area inside corridor
# define region
gs.run_command("g.region", flags = "ap", raster = "corredor_SP1_buffer_30m_null", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "corredor_SP1_buffer_30m_null")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_SP1_area.csv", separator = "comma", overwrite = True)



## area inside corridor and imoveis
# rasterize
gs.mapcalc("suzano_properties_30m_inside_SP1 = suzano_properties_30m", overwrite = True)
gs.mapcalc("suzano_properties_30m_inside_SP1_bin = suzano_properties_30m_inside_SP1", overwrite = True)
gs.run_command("r.null", map = "suzano_properties_30m_inside_SP1_bin", null = 0)
gs.mapcalc("suzano_properties_30m_outside_SP1 = if(suzano_properties_30m_inside_SP1_bin == 0, 1, null())", overwrite = True)

## area inside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_inside_SP1", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_inside_SP1")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_SP1_inside_area.csv", separator = "comma", overwrite = True)


## area inside corridor and ouside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_outside_SP1", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_outside_SP1")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_SP1_outside_area.csv", separator = "comma", overwrite = True)



# sp2 ------------------------------------------------------------------------- #
dir_a = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/05_area"
os.chdir(dir_a)

# define region
gs.run_command("g.region", flags = "ap", vector = "bacia_nivel5_corredor_SP2", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "bacia_nivel5_corredor_SP2")

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_SP2", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_SP2", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_SP2", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2.csv", separator = "comma", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2_ha = mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2 * 0.09"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

# vectorize area
gs.run_command("r.to.vect", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2_ha", type = "area", column = "area_ha", overwrite = True)

# select area vector overlap with corridor
gs.run_command("v.select", ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2_ha", binput = "corredor_SP2_buffer",
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2_ha_corredor_buffer", operator = "overlap", overwrite = True)

# export vector
gs.run_command("v.out.ogr", input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2_ha_corredor_buffer", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_SP2_ha_corredor_buffer.shp", format = "ESRI_Shapefile", overwrite = True)



# corridor
gs.run_command("v.to.rast", input = "corredor_SP2_buffer", output = "corredor_SP2_buffer_30m_null", use = "val", value = 1, overwrite = True)

gs.run_command("v.to.rast", input = "corredor_SP2_buffer", output = "corredor_SP2_buffer_30m", use = "val", value = 1, overwrite = True)
gs.run_command("r.null", map = "corredor_SP2_buffer_30m", null = 0, overwrite = True)

# add corridor to mapbiomas and suzano
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer = mapbiomas_2019_30m_rec_forest_suzano + corredor_SP2_buffer_30m", overwrite = True)
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer_null = if(mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer > 0, 1, null())", overwrite = True)

# clump
gs.run_command("r.clump", flags = "d", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer_null", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer_null_clump_SP2", overwrite = True)

# area
gs.run_command("r.area", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer_null_clump_SP2", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer_null_area_SP2", overwrite = True)

# area
gs.run_command("r.stats", flags = "aln", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer_null_clump_SP2", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer_null_area_SP2.csv", separator = "comma", overwrite = True)

# area in hectares
ex = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer_null_area_SP2_ha = mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer_null_area_SP2 * 0.09"
gs.mapcalc(ex, overwrite = True)

# export
gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer_null_area_SP2_ha", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_corredor_SP2_buffer_null_area_SP2_ha.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)



# area inside corridor
# define region
gs.run_command("g.region", flags = "ap", raster = "corredor_SP2_buffer_30m_null", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "corredor_SP2_buffer_30m_null")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_SP2_area.csv", separator = "comma", overwrite = True)



## area inside corridor and imoveis
# rasterize
gs.mapcalc("suzano_properties_30m_inside_SP2 = suzano_properties_30m", overwrite = True)
gs.mapcalc("suzano_properties_30m_inside_SP2_bin = suzano_properties_30m_inside_SP2", overwrite = True)
gs.run_command("r.null", map = "suzano_properties_30m_inside_SP2_bin", null = 0)
gs.mapcalc("suzano_properties_30m_outside_SP2 = if(suzano_properties_30m_inside_SP2_bin == 0, 1, null())", overwrite = True)

## area inside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_inside_SP2", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_inside_SP2")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_SP2_inside_area.csv", separator = "comma", overwrite = True)


## area inside corridor and ouside imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "suzano_properties_30m_outside_SP2", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "suzano_properties_30m_outside_SP2")

# area
gs.run_command("r.stats", flags = "alnp", input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_corredor_SP2_outside_area.csv", separator = "comma", overwrite = True)

# export clump ------------------------------------------------------------------------- #
for i in ["BAMGES", "MA", "MS", "SP1", "SP2"]:
    print(i)
    gs.run_command("g.region", flags = "ap", vector = "bacia_nivel5_corredor_" + i, res = 30)
    gs.run_command("r.mask", flags = "r")
    gs.run_command("r.mask", vector = "bacia_nivel5_corredor_" + i)
    gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_" + i, \
        output = "mapbiomas_2019_30m_rec_forest_suzano_null_clump_" + i + ".tif", \
        format = "GTiff", createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

# end -------------------------------------------------------------------------- #