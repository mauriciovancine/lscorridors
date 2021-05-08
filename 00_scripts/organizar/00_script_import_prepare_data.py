#' -----
#' objetivos: importar, reprojetar, reclassificar e exportar raster
#' autor: mauricio vancine
#' data: 2020-11-14
#' -----

# iniciar o python
python3

# importar bibliotecas
import os
import grass.script as gs

# ------------------------------------------------------------------------------- #
# import vector corridors
dir_v = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/corredores"
os.chdir(dir_v)
for i in os.listdir(dir_v):
    if i.endswith(".shp"):
        i_ou = i.replace(".shp", "")
        gs.run_command("v.import", input = i, output = i_ou, overwrite = True)
        gs.run_command("v.buffer", input = i_ou, output = i_ou + "_buffer", distance = 500, overwrite = True)    

# import study areas 
dir_v = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/unfs"
os.chdir(dir_v)
for i in os.listdir(dir_v):
    if i.endswith(".shp"):
        i_ou = i.replace(".shp", "")
        gs.run_command("v.import", input = i, output = i_ou, overwrite = True)
        gs.run_command("v.db.addcolumn", map = i_ou, column = "val text", quiet = True)
        gs.run_command("v.db.update", map = i_ou, column = "val", value = "1", quiet = True)
        gs.run_command("v.dissolve", input = i_ou, column = "val", output = i_ou, overwrite = True)

# import vector suzano forest
dir_v = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/Base_MAF_2020_03"
os.chdir(dir_v)
gs.run_command("v.import", input = "matricula_vegetacao.shp", output = "suzano_forest", overwrite = True)

# import imoveis
dir_v = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/imóveis"
os.chdir(dir_v)
gs.run_command("v.import", input = "imoveis_albers.shp", output = "suzano_properties", overwrite = True)

# import rasters
dir_r = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/03_raster"
os.chdir(dir_r)
for i in os.listdir(dir_r):
    if i.endswith(".tif"):
        i_in = i
        i_ou = i.replace(".tif", "")
        print(i_in)
        print(i_ou)
        gs.run_command("r.import", input = i_in, output = i_ou, overwrite = True)

# rename
gs.run_command("g.rename", raster = ["COLECAO_5_DOWNLOADS_COLECOES_ANUAL_CAATINGA_CAATINGA-2019", "caatinga"])
gs.run_command("g.rename", raster = ["COLECAO_5_DOWNLOADS_COLECOES_ANUAL_AMAZONIA_AMAZONIA-2019", "amazonia"])
gs.run_command("g.rename", raster = ["COLECAO_5_DOWNLOADS_COLECOES_ANUAL_MATAATLANTICA_MATAATLANTICA-2019", "mata_atlantica"])
gs.run_command("g.rename", raster = ["COLECAO_5_DOWNLOADS_COLECOES_ANUAL_CERRADO_CERRADO-2019", "cerrado"])
gs.run_command("g.rename", raster = ["COLECAO_5_DOWNLOADS_COLECOES_ANUAL_PAMPA_PAMPA-2019", "pampa"])
gs.run_command("g.rename", raster = ["COLECAO_5_DOWNLOADS_COLECOES_ANUAL_PANTANAL_PANTANAL-2019", "pantanal"])

# 30 m -------------------------------------------------------------------------- #
# verify region
gs.run_command("g.region", flags = "p")

# define region
gs.run_command("g.region", flags = "ap", raster = ["amazonia", "cerrado", "caatinga", "mata_atlantica", "pantanal", "pampa"], res = 30)

# raster calculate - resolution and na's
for i in ["amazonia", "cerrado", "caatinga", "mata_atlantica", "pantanal", "pampa"]:
    print(i)
    gs.mapcalc(i + "_30m = if(" + i + " == 0, null(), " + i + ")", overwrite = True)

# mosaic
gs.run_command("r.patch", input = ["caatinga_30m", "amazonia_30m", "mata_atlantica_30m", "cerrado_30m", "pantanal_30m", "pampa_30m"], output = "mapbiomas_2019_30m", overwrite = True)

# reclassify cover
gs.run_command("r.reclass", input = "mapbiomas_2019_30m", output = "mapbiomas_2019_30m_rec", rules = "reclass_mapbiomas_v5.txt", overwrite = True)

# rasterize
gs.run_command("v.to.rast", input = "suzano_forest", output = "suzano_forest_30m", use = "val", value = 1, overwrite = True)
gs.run_command("r.null", map = "suzano_forest_30m", null = 0, overwrite = True)

# integrate mapbiomas and suzano
gs.mapcalc("mapbiomas_2019_30m_rec_forest = if(mapbiomas_2019_30m_rec == 1, 1, 0)", overwrite = True)
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano = mapbiomas_2019_30m_rec_forest + suzano_forest_30m", overwrite = True)
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_null = if(mapbiomas_2019_30m_rec_forest_suzano > 0, 1, null())", overwrite = True)
gs.mapcalc("mapbiomas_2019_30m_rec_forest_suzano_mapbiomas = if(mapbiomas_2019_30m_rec_forest_suzano_forest == 1, 1, mapbiomas_2019_30m_rec)", overwrite = True)

# rasterize suzano properties
gs.run_command("v.to.rast", input = "suzano_properties", output = "suzano_properties_30m", use = "val", value = 1, overwrite = True)

# draft ------------------------------------------------------------------------ #
# import basin
# dir_v = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/nivel_5"
# os.chdir(dir_v)
# gs.run_command("v.import", input = "nivel_5.shp", output = "bacia_nivel5", overwrite = True)

# import study areas 
# gs.run_command("g.remove", flags = "f", type = "vector", pattern = "bacia_nivel5*")

# li_co = gs.list_grouped("vector", pattern = "corredor_*")["PERMANENT"]
# or i in li_co:
#     i_ou = "bacia_nivel5_" + i
#     gs.run_command("v.select", ainput = "bacia_nivel5", binput = i, output = i_ou, operator = "overlap", overwrite = True)
#     gs.run_command("v.db.addcolumn", map = i_ou, column = "val text", quiet = True)
#     gs.run_command("v.db.update", map = i_ou, column = "val", value = "1", quiet = True)
#     gs.run_command("v.dissolve", input = i_ou, column = "val", output = i_ou, overwrite = True)

# export
# dir_v = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/area_estudo"
# os.chdir(dir_v)
# li_co = gs.list_grouped("vector", pattern = "bacia_nivel5_corredor_*")["PERMANENT"]
# for i in li_co:
#     gs.run_command("v.out.ogr", input = i, output = i + ".shp", format = "ESRI_Shapefile", overwrite = True)

# end -------------------------------------------------------------------------- #