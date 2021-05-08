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

# define region
gs.run_command("g.region", flags = "ap", vector = "suzano_properties", res = 30)

# suzano
gs.run_command("v.db.addcolumn", map = "suzano_properties", column = "val int")
gs.run_command("v.db.update", map = "suzano_properties", column = "val", value = 1)
gs.run_command("v.dissolve", input = "suzano_properties", output = "suzano_properties_diss", column = "val", overwrite = True)

# bamges ------------------------------------------------------------------------- #
# directory
dir_bamges = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/10_corredores_imoveis/bamges"
os.chdir(dir_bamges)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_bamges_mask")

# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_outside_imoveis", \
    operator = "not", overwrite = True)


# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_outside_imoveis", \
    operator = "not", overwrite = True)


# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_outside_imoveis", \
    operator = "not", overwrite = True)


# remove columns
gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_inside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_outside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_inside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_outside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_inside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_outside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

# area
gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")


# export
gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer500m_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer250m_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_bamges_ha_corredor_buffer45m_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)




# ma ------------------------------------------------------------------------- #
# directory
dir_ma = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/10_corredores_imoveis/ma"
os.chdir(dir_ma)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ma_mask", res = 30)


# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_outside_imoveis", \
    operator = "not", overwrite = True)


# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_outside_imoveis", \
    operator = "not", overwrite = True)

# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_outside_imoveis", \
    operator = "not", overwrite = True)


# remove columns
gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_inside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_outside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_inside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_outside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_inside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_outside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

# area
gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")


# export
gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer500m_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer250m_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ma_ha_corredor_buffer45m_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)


# ms ------------------------------------------------------------------------- #
# directory
dir_ms = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/10_corredores_imoveis/ms"
os.chdir(dir_ms)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ms_mask", res = 30)


# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_outside_imoveis", \
    operator = "not", overwrite = True)


# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_outside_imoveis", \
    operator = "not", overwrite = True)


# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_outside_imoveis", \
    operator = "not", overwrite = True)


# remove columns
gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_inside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_outside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_inside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_outside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_inside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_outside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])


# area
gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", units = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", units = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", units = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", units = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", units = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", units = "h")



# export
gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer500m_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer250m_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_ms_ha_corredor_buffer45m_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)


# end -------------------------------------------------------------------------- #