#" -----
#" objetivos: importar, reprojetar, reclassificar e exportar raster
#" autor: mauricio vancine
#" data: 2020-11-30
#" -----

# iniciar o python
python

# importar bibliotecas
import os, glob
import grass.script as gs

# bamges corridors ------------------------------------------------------------------------- #
# directory
dir_v = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corridors/bamges/corridor_90m/"
os.chdir(dir_v)

dirs = glob.glob("*/")
dirs

for j in dirs:
	os.chdir(dir_v + j)
	for i in glob.glob("*"):
		if i.endswith(".shp"):
			i_ou = i.replace(".shp", "")
        	gs.run_command("v.import", input = i, output = i_ou, overwrite = True)
        	gs.run_command("v.out.ogr", input = i_ou, 
        		output = "/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corridors/bamges/corridors_vector/" + i, \
        		format = "ESRI_Shapefile", overwrite = True)


# ma corridors ------------------------------------------------------------------------- #
# directory
dir_v = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corridors/ma/corridor_90m/"
os.chdir(dir_v)

dirs = glob.glob("*/")
dirs

for j in dirs:
	os.chdir(dir_v + j)
	for i in glob.glob("*"):
		if i.endswith(".shp"):
			i_ou = i.replace(".shp", "")
        	gs.run_command("v.import", input = i, output = i_ou, overwrite = True)
        	gs.run_command("v.out.ogr", input = i_ou, 
        		output = "/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corridors/ma/corridors_vector/" + i, \
        		format = "ESRI_Shapefile", overwrite = True)


# ms corridors ------------------------------------------------------------------------- #
# directory
dir_v = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corridors/ms/corridor_90m/"
os.chdir(dir_v)

dirs = glob.glob("*/")
dirs

for j in dirs:
	os.chdir(dir_v + j)
	for i in glob.glob("*.shp"):
			i_ou = i.replace(".shp", "")
			i_out = i_ou.replace("mapbiomas_2019_30m_rec_suzano_forest_wei_ms_90m_", "ms_")
			gs.run_command("v.import", input = i, output = i_ou, overwrite = True)
			gs.run_command("v.out.ogr", input = i_ou, \
				output = "/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corridors/ms/corridors_vector/" + i_out + ".shp", \
				format = "ESRI_Shapefile", overwrite = True)


# end -------------------------------------------------------------------------- #