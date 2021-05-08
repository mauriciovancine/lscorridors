# 300 m ------------------------------------------------------------------------- #
# verify region
gs.run_command("g.region", flags = "p")

# define region
gs.run_command("g.region", flags = "ap", raster = ["amazonia", "cerrado", "caatinga", "mata_atlantica", "pantanal", "pampa"], res = 300)

# raster calculate - resolution and na's
# gs.run_command("g.remove", flags = "f", type = "raster", pattern = "*300m")
for i in ["amazonia", "cerrado", "caatinga", "mata_atlantica", "pantanal", "pampa"]:
    print(i)
    gs.mapcalc(i + "_300m = if(" + i + " == 0, null(), " + i + ")", overwrite = True)

# mosaic
gs.run_command("r.patch", input = ["caatinga_300m", "amazonia_300m", "mata_atlantica_300m", "cerrado_300m", "pantanal_300m", "pampa_300m"], output = "mapbiomas_2019_300m", overwrite = True)

# reclassify cover
gs.run_command("r.reclass", input = "mapbiomas_2019_300m", output = "mapbiomas_2019_300m_rec", rules = "reclass_mapbiomas_v5.txt", overwrite = True)

# reclassify weight
# gs.run_command("r.reclass", input = "mapbiomas_2019_300m_rec", output = "mapbiomas_2019_300m_wei", rules = "reclass_weight.txt")

# rasterize
gs.run_command("v.to.rast", input = "matricula_vegetacao", output = "matricula_vegetacao_300m", use = "val", value = 1, overwrite = True)



# 200 m ------------------------------------------------------------------------- #
# verify region
gs.run_command("g.region", flags = "p")

# define region
gs.run_command("g.region", flags = "ap", raster = ["amazonia", "cerrado", "caatinga", "mata_atlantica", "pantanal", "pampa"], res = 200)

# raster calculate - resolution and na's
for i in ["amazonia", "cerrado", "caatinga", "mata_atlantica", "pantanal", "pampa"]:
    print(i)
    gs.mapcalc(i + "_200m = if(" + i + " == 0, null(), " + i + ")", overwrite = True)

# mosaic
gs.run_command("r.patch", input = ["caatinga_200m", "amazonia_200m", "mata_atlantica_200m", "cerrado_200m", "pantanal_200m", "pampa_200m"], output = "mapbiomas_2019_200m", overwrite = True)

# reclassify cover
gs.run_command("r.reclass", input = "mapbiomas_2019_200m", output = "mapbiomas_2019_200m_rec", rules = "reclass_mapbiomas_v5.txt", overwrite = True)

# reclassify weight
# gs.run_command("r.reclass", input = "mapbiomas_2019_200m_rec", output = "mapbiomas_2019_200m_wei", rules = "reclass_weight.txt")

# rasterize
gs.run_command("v.to.rast", input = "matricula_vegetacao", output = "matricula_vegetacao_200m", use = "val", value = 1, overwrite = True)



# 100 m ------------------------------------------------------------------------- #
# verify region
gs.run_command("g.region", flags = "p")

# define region
gs.run_command("g.region", flags = "ap", raster = ["amazonia", "cerrado", "caatinga", "mata_atlantica", "pantanal", "pampa"], res = 100)

# raster calculate - resolution and na's
for i in ["amazonia", "cerrado", "caatinga", "mata_atlantica", "pantanal", "pampa"]:
    print(i)
    gs.mapcalc(i + "_100m = if(" + i + " == 0, null(), " + i + ")", overwrite = True)

# mosaic
gs.run_command("r.patch", input = ["caatinga_100m", "amazonia_100m", "mata_atlantica_100m", "cerrado_100m", "pantanal_100m", "pampa_100m"], output = "mapbiomas_2019_100m", overwrite = True)

# reclassify cover
gs.run_command("r.reclass", input = "mapbiomas_2019_100m", output = "mapbiomas_2019_100m_rec", rules = "reclass_mapbiomas_v5.txt", overwrite = True)

# reclassify weight
# gs.run_command("r.reclass", input = "mapbiomas_2019_100m_rec", output = "mapbiomas_2019_100m_wei", rules = "reclass_weight.txt")

# rasterize
gs.run_command("v.to.rast", input = "matricula_vegetacao", output = "matricula_vegetacao_100m", use = "val", value = 1, overwrite = True)


# 90 m ------------------------------------------------------------------------- #
# verify region
gs.run_command("g.region", flags = "p")

# define region
gs.run_command("g.region", flags = "ap", raster = ["amazonia", "cerrado", "caatinga", "mata_atlantica", "pantanal", "pampa"], res = 90)

# raster calculate - resolution and na's
for i in ["amazonia", "cerrado", "caatinga", "mata_atlantica", "pantanal", "pampa"]:
    print(i)
    gs.mapcalc(i + "_90m = if(" + i + " == 0, null(), " + i + ")", overwrite = True)

# mosaic
gs.run_command("r.patch", input = ["caatinga_90m", "amazonia_90m", "mata_atlantica_90m", "cerrado_90m", "pantanal_90m", "pampa_90m"], output = "mapbiomas_2019_90m", overwrite = True)

# reclassify cover
gs.run_command("r.reclass", input = "mapbiomas_2019_90m", output = "mapbiomas_2019_90m_rec", rules = "reclass_mapbiomas_v5.txt", overwrite = True)

# reclassify weight
# gs.run_command("r.reclass", input = "mapbiomas_2019_90m_rec", output = "mapbiomas_2019_90m_wei", rules = "reclass_weight.txt")

# rasterize
gs.run_command("v.to.rast", input = "matricula_vegetacao", output = "matricula_vegetacao_90m", use = "val", value = 1, overwrite = True)
gs.run_command("r.null", map = "matricula_vegetacao_90m", null = 0, overwrite = True)

# integrate mapbiomas and suzano
gs.mapcalc("mapbiomas_2019_90m_rec_forest = if(mapbiomas_2019_90m_rec == 1, 1, 0)", overwrite = True)
gs.mapcalc("mapbiomas_2019_90m_rec_suzano = mapbiomas_2019_90m_rec_forest + matricula_vegetacao_90m", overwrite = True)
gs.mapcalc("mapbiomas_2019_90m_rec_suzano_null = if(mapbiomas_2019_90m_rec_suzano > 0, 1, null())", overwrite = True)
gs.mapcalc("mapbiomas_2019_90m_rec_suzano = if(mapbiomas_2019_90m_rec_suzano > 0, 1, 0)", overwrite = True)
gs.mapcalc("mapbiomas_2019_90m_rec_suzano_mapbiomas = if(mapbiomas_2019_90m_rec_suzano == 1, 1, mapbiomas_2019_90m_rec)", overwrite = True)