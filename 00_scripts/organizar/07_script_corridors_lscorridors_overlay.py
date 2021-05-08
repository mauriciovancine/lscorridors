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
# directory
dir_corr_bamges = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corridors_area_v02/bamges"
os.chdir(dir_corr_bamges)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_bamges_mask", res = 90)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_bamges_mask")

# target to vector
gs.run_command("r.to.vect", input = "target_bamges_90m", output = "target_bamges_90m", \
	type = "area", column = "target", overwrite = True)

# export vector
gs.run_command("v.out.ogr", input = "target_bamges_90m", \
    output = "target_bamges_90m.shp", format = "ESRI_Shapefile", overwrite = True)

# import corridors
dir_corr_in_bamges = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/06_corridors_lscorridos/ma/corridor_vector_union/00_raw"
dir_corr_out_bamges = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/06_corridors_lscorridos/ma/corridor_vector_union/01_overlay_target"

os.chdir(dir_corr_in_bamges)

for i in glob.glob("*.shp"):
	i_ou = i.replace(".shp", "")
	os.chdir(dir_corr_in_bamges)
	gs.run_command("v.in.ogr", flags = "o", input = i, output = i_ou, overwrite = True)
	gs.run_command("v.overlay", ainput = i_ou, binput = "target_bamges_90m", \
		output = i_ou + "_overlay_target", operator = "not", overwrite = True)
	os.chdir(dir_corr_out_bamges)
	gs.run_command("v.out.ogr", input = i_ou + "_overlay_target", \
		output = i_ou + "_overlay_target.shp", format = "ESRI_Shapefile", overwrite = True)
	gs.run_command("g.remove", flags = "f", type = "vector", name = i_ou)
	gs.run_command("g.remove", flags = "f", type = "vector", name = i_ou + "_overlay_target")






# ma ------------------------------------------------------------------------- #
# directory
dir_corr_ma = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corridors_area_v02/ma"
os.chdir(dir_corr_ma)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ma_mask", res = 90)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_ma_mask")

# target to vector
gs.run_command("r.to.vect", input = "target_ma_90m", output = "target_ma_90m", \
	type = "area", column = "target", overwrite = True)

# export vector
gs.run_command("v.out.ogr", input = "target_ma_90m", \
    output = "target_ma_90m.shp", format = "ESRI_Shapefile", overwrite = True)

# import corridors
dir_corr_in_ma = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/06_corridors_lscorridos/ma/corridor_vector_union/00_raw"
dir_corr_out_ma = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/06_corridors_lscorridos/ma/corridor_vector_union/01_overlay_target"

os.chdir(dir_corr_in_ma)

for i in glob.glob("*.shp"):
	i_ou = i.replace(".shp", "")
	os.chdir(dir_corr_in_ma)
	gs.run_command("v.in.ogr", flags = "o", input = i, output = i_ou, overwrite = True)
	gs.run_command("v.overlay", ainput = i_ou, binput = "target_ma_90m", \
		output = i_ou + "_overlay_target", operator = "not", overwrite = True)
	os.chdir(dir_corr_out_ma)
	gs.run_command("v.out.ogr", input = i_ou + "_overlay_target", \
		output = i_ou + "_overlay_target.shp", format = "ESRI_Shapefile", overwrite = True)
	gs.run_command("g.remove", flags = "f", type = "vector", name = i_ou)
	gs.run_command("g.remove", flags = "f", type = "vector", name = i_ou + "_overlay_target")



# ms ------------------------------------------------------------------------- #
# directory
dir_corr_ms = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/07_corridors_area_v02/ms"
os.chdir(dir_corr_ms)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ms_mask", res = 90)

# define mask
gs.run_command("r.mask", flags = "r")
gs.run_command("r.mask", vector = "unf_ms_mask")

# target to vector
gs.run_command("r.to.vect", input = "target_ms_90m", output = "target_ms_90m", \
	type = "area", column = "target", overwrite = True)

# export vector
gs.run_command("v.out.ogr", input = "target_ms_90m", \
    output = "target_ms_90m.shp", format = "ESRI_Shapefile", overwrite = True)

# import corridors
dir_corr_in_ms = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/06_corridors_lscorridos/ms/corridor_vector_union/00_raw"
dir_corr_out_ms = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/06_corridors_lscorridos/ms/corridor_vector_union/01_overlay_target"

os.chdir(dir_corr_in_ms)

for i in glob.glob("*.shp"):
	i_ou = i.replace(".shp", "")
	os.chdir(dir_corr_in_ms)
	gs.run_command("v.in.ogr", flags = "o", input = i, output = i_ou, overwrite = True)
	gs.run_command("v.overlay", ainput = i_ou, binput = "target_ms_90m", \
		output = i_ou + "_overlay_target", operator = "not", overwrite = True)
	os.chdir(dir_corr_out_ms)
	gs.run_command("v.out.ogr", input = i_ou + "_overlay_target", \
		output = i_ou + "_overlay_target.shp", format = "ESRI_Shapefile", overwrite = True)
	gs.run_command("g.remove", flags = "f", type = "vector", name = i_ou)
	gs.run_command("g.remove", flags = "f", type = "vector", name = i_ou + "_overlay_target")


# end -------------------------------------------------------------------------- #