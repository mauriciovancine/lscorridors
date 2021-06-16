#" -----
#" objetivos: importar, reprojetar, reclassificar e exportar raster
#" autor: mauricio vancine
#" data: 24-10-2020
#" -----

# iniciar o python
python3

# import libs
import os, fnmatch, imp
import grass.script as gs

# directory
path = r"/home/mude/data/github/lscorridors/"

# import lscorridors
os.chdir(path + "lscorridors")
r_ls_corridors = imp.load_source("main", "r_ls_corridors_v1_0_4.py")

# addons
# gs.run_command("g.extension", extension = "v.centerpoint")

# --------------------------------------------------------------------------------

## import data

# directory
os.chdir(path + "01_data")

# import vector
gs.run_command("v.in.ogr", 
  input = "rio_claro_limit_sirgas2000_utm23s.shp",
  output = "limit_rc", 
  overwrite = True)

gs.run_command("v.in.ogr", 
  input = "source_target_sirgas2000_utm23s.shp",
  output = "source_target", 
  overwrite = True)

# import raster
gs.run_command("r.import", 
  input = "mapbiomas_c5_2019_mataatlantica_rio_claro_wgs84_geo.tif",
  output = "mapbiomas_af",
  overwrite = True)

# import raster
gs.run_command("r.import", 
  input = "mapbiomas_c5_2019_cerrado_rio_claro_wgs84_geo.tif",
  output = "mapbiomas_ce",
  overwrite = True)

# --------------------------------------------------------------------------------

## prepare data

# define region and resolution
gs.run_command("g.region", flags = "ap", vector = "limit_rc", res = 30)

# create maps with resolution from region
gs.mapcalc("mapbiomas_af_30m = mapbiomas_af", overwrite = True)
gs.mapcalc("mapbiomas_ce_30m = mapbiomas_ce", overwrite = True)

# merge rasters
gs.run_command("r.patch", flags = "z", 
	input = ["mapbiomas_af_30m", "mapbiomas_ce_30m"], 
	output = "mapbiomas_30m", overwrite = True)

# reclassify raster to habitat
gs.run_command("r.reclass", 
	input = "mapbiomas_30m", 
	output = "mapbiomas_30m_use", 
	rules = "reclass_mapbiomas_v5.txt", 
	overwrite = True)

# reclassify raster to weight
gs.run_command("r.reclass", 
	input = "mapbiomas_30m_use", 
	output = "mapbiomas_30m_weight", 
	rules = "reclass_mapbiomas_v5_weight.txt", 
	overwrite = True)


# centroids targets
gs.run_command("v.centerpoint", 
  input = "source_target",
  output = "source_target_centroids",
  overwrite = True)


# rasterize targets
gs.run_command("v.to.rast", 
  input = "source_target",
  output = "source_target", 
  use = "cat",
  overwrite = True)

gs.run_command("v.to.rast", 
  input = "source_target_centroids",
  output = "source_target_centroids", 
  use = "cat",
  overwrite = True)


# -------------------------------------------------------------------------

# target pairs to be connected
pairs = "1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10"

# output directory
path_out = path + "02_corridors"

# run corridors
r_ls_corridors.main(
	resistancemap = "mapbiomas_30m_weight", 
	stmap = "source_target", 
	stlist = "1,2,2,3", 
	output_prefix = "", 
	output_folder = path_out, 
	variability = "2.0", 
	scale = "100", 
	simulations = "2",
	method = "MP"
	)

# run corridors
r_ls_corridors.main(
	resistancemap = "mapbiomas_30m_weight", 
	stmap = "source_target_centroids", 
	stlist = "1,2,2,3", 
	output_prefix = "", 
	output_folder = path + "02_corridors_centroids", 
	variability = "2.0", 
	scale = "100", 
	simulations = "2",
	method = "MP"
	)


# end -------------------------------------------------------------------------- #