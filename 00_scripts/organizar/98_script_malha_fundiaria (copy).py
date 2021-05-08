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

# directory
dir_malha = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/MalhaFundiaria_LandTenure_v.1812"
os.chdir(dir_malha)

# bamges
gs.run_command("r.import", \
    input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges.tif", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges", \
    overwrite = True)

# ma
gs.run_command("r.import", \
    input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma.tif", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma", \
    overwrite = True)

# ms
gs.run_command("r.import", \
    input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms.tif", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms", \
    overwrite = True)



# bamges ------------------------------------------------------------------------- #
# directory
dir_bamges = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/MalhaFundiaria_LandTenure_v.1812/bamges"
os.chdir(dir_bamges)


# define region
gs.run_command("g.region", flags = "ap", vector = "unf_bamges_mask", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_bamges_mask")

# mapcalc
gs.mapcalc("pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges_albers_30m = pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges", overwrite = True)

# export raster
gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges_albers_30m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)

# vetorize
gs.run_command("r.to.vect", \
	input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges_albers_30m", \
    type = "area", \
    column = "subclasse", \
    overwrite = True)

# export vector
gs.run_command("v.out.ogr", \
    input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges_albers_30m.shp", \
    format = "ESRI_Shapefile", \
    overwrite = True)

# corredor e imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "corr_bamges_buffer500m_30m_null", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "corr_bamges_buffer500m_30m_null")

# rasterize corridor and imoveis
gs.mapcalc("suzano_properties_30m_inside_bamges_buffer500m = suzano_properties_30m", overwrite = True)
gs.mapcalc("suzano_properties_30m_inside_bamges_bin_buffer500m = suzano_properties_30m_inside_bamges_buffer500m", overwrite = True)
gs.run_command("r.null", map = "suzano_properties_30m_inside_bamges_bin_buffer500m", null = 0)

# export raster
gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "suzano_properties_30m_inside_bamges_bin_buffer500m", \
    output = "suzano_properties_30m_inside_bamges_bin_buffer500m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)

gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_bamges_albers_30m_buffer500m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)

gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_bamges_buffer500m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)






# ma ------------------------------------------------------------------------- #
# directory
dir_ma = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/MalhaFundiaria_LandTenure_v.1812/ma"
os.chdir(dir_ma)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ma_mask", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_ma_mask")

# mapcalc
gs.mapcalc("pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma_albers_30m = pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma", overwrite = True)

# export raster
gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma_albers_30m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)

# vetorize
gs.run_command("r.to.vect", \
	input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma_albers_30m", \
    type = "area", \
    column = "subclasse", \
    overwrite = True)

# export vector
gs.run_command("v.out.ogr", \
    input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma_albers_30m.shp", \
    format = "ESRI_Shapefile", \
    overwrite = True)

# corredor e imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "corr_ma_buffer500m_30m_null", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "corr_ma_buffer500m_30m_null")

# rasterize corridor and imoveis
gs.mapcalc("suzano_properties_30m_inside_ma_buffer500m = suzano_properties_30m", overwrite = True)
gs.mapcalc("suzano_properties_30m_inside_ma_bin_buffer500m = suzano_properties_30m_inside_ma_buffer500m", overwrite = True)
gs.run_command("r.null", map = "suzano_properties_30m_inside_ma_bin_buffer500m", null = 0)

# export raster
gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "suzano_properties_30m_inside_ma_bin_buffer500m", \
    output = "suzano_properties_30m_inside_ma_bin_buffer500m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)

gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ma_albers_30m_buffer500m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)

gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_ma_buffer500m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)







# ms ------------------------------------------------------------------------- #
# directory
dir_ms = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/MalhaFundiaria_LandTenure_v.1812/ms"
os.chdir(dir_ms)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ms_mask", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_ms_mask")

# mapcalc
gs.mapcalc("pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms_albers_30m = pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms", overwrite = True)

# export raster
gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms_albers_30m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)

# vetorize
gs.run_command("r.to.vect", \
	input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms_albers_30m", \
    type = "area", \
    column = "subclasse", \
    overwrite = True)

# export vector
gs.run_command("v.out.ogr", \
    input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms_albers_30m.shp", \
    format = "ESRI_Shapefile", \
    overwrite = True)

# corredor e imoveis
# define region
gs.run_command("g.region", flags = "ap", raster = "corr_ms_buffer500m_30m_null", res = 30)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", raster = "corr_ms_buffer500m_30m_null")

# rasterize corridor and imoveis
gs.mapcalc("suzano_properties_30m_inside_ms_buffer500m = suzano_properties_30m", overwrite = True)
gs.mapcalc("suzano_properties_30m_inside_ms_bin_buffer500m = suzano_properties_30m_inside_ms_buffer500m", overwrite = True)
gs.run_command("r.null", map = "suzano_properties_30m_inside_ms_bin_buffer500m", null = 0)

# export raster
gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "suzano_properties_30m_inside_ms_bin_buffer500m", \
    output = "suzano_properties_30m_inside_ms_bin_buffer500m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)

gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms_albers_30m", \
    output = "pa_br_landtenure_rnd_wo_categ_30m_2018_imaflora_ms_albers_30m_buffer500m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)

gs.run_command("r.out.gdal", \
	flags = "c", \
	input = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_mapbiomas_ms_buffer500m.tif", \
    format = "GTiff", \
    createopt = "TFW=YES,COMPRESS=DEFLATE", \
    overwrite = True)

# end -------------------------------------------------------------------------- #