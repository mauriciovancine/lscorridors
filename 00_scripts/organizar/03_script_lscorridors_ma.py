#" -----
#" objetivos: importar, reprojetar, reclassificar e exportar raster
#" autor: mauricio vancine
#" data: 24-10-2020
#" -----

# iniciar o python
python

# importar bibliotecas
import os, fnmatch, imp
import grass.script as gs


# ma corridors ------------------------------------------------------------------------- #
# directory
dir_raster = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/03_raster"
os.chdir(dir_raster)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ma_mask", res = 90)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_ma_mask")

# directory
dir_raster = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/00_targets"
os.chdir(dir_raster)
gs.run_command("v.import", input = "target_ma.shp", output = "target_ma", overwrite = True)

# rasterize targets
gs.run_command("v.to.rast", input = "target_ma", output = "target_ma_90m", use = "attr", attribute_column = "target", overwrite = True)

# prepare mapbiomas and suzano forest
gs.mapcalc("mapbiomas_2019_30m_rec_suzano_forest_ma_90m = if(suzano_forest_30m == 1, 6, mapbiomas_2019_30m_rec)", overwrite = True)

# reclassify weight
gs.run_command("r.reclass", input = "mapbiomas_2019_30m_rec_suzano_forest_ma_90m", output = "mapbiomas_2019_30m_rec_suzano_forest_wei_ma_90m", rules = "reclass_mapbiomas_v5_weight.txt")

# export
di_out = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corridors/ma"
os.chdir(di_out)

gs.run_command("r.out.gdal", flags = "c", input = "target_ma_90m", \
    output = "target_ma_90m.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_suzano_forest_ma_90m", \
    output = "mapbiomas_2019_30m_rec_suzano_forest_ma_90m.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)

gs.run_command("r.out.gdal", flags = "c", input = "mapbiomas_2019_30m_rec_suzano_forest_wei_ma_90m", \
    output = "mapbiomas_2019_30m_rec_suzano_forest_wei_ma_90m.tif", format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", overwrite = True)


# run lscorridors
# directory
di = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/ls_corridors_mhv"
os.chdir(di)

# import modules
r_ls_corridors = imp.load_source("main", "r_ls_corridors_v1_0_3.py")

# target pairs to be connected
pairs = "1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23"

# output directory
di_out = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corridors/ma/corridor_90m"

# run corridors
r_ls_corridors.main(
	resistancemap = "mapbiomas_2019_30m_rec_suzano_forest_wei_ma_90m", 
	stmap = "target_ma_90m", 
	stlist = pairs, 
	output_prefix = "", 
	output_folder = di_out, 
	variability = "2.0", 
	scale = "100", 
	simulations = "100", 
	method = "MP"
	)
        




# end -------------------------------------------------------------------------- #