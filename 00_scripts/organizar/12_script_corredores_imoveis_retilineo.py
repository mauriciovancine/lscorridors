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
dir_malha = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/10_corredores_imoveis/retilineo"
os.chdir(dir_malha)


# bamges ------------------------------------------------------------------------- #
# define region
gs.run_command("g.region", flags = "ap", vector = "unf_bamges_mask", res = 30)

# suzano
gs.run_command("v.db.addcolumn", map = "suzano_properties", column = "val int")
gs.run_command("v.db.update", map = "suzano_properties", column = "val", value = 1)
gs.run_command("v.dissolve", input = "suzano_properties", output = "suzano_properties_diss", column = "val")

# retilineo
# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_outside_imoveis", \
    operator = "not", overwrite = True)

# remove columns
gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_inside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_outside_imoveis", \
    columns = ["a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])


# area
gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

# export
gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_BAMGES_ha_corredor_buffer_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)


# MA ------------------------------------------------------------------------- #
# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ma_mask", res = 30)

# retilineo
# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_outside_imoveis", \
    operator = "not", overwrite = True)

# remove columns
gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_inside_imoveis", \
    columns = ["a_cat", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_outside_imoveis", \
    columns = ["a_cat", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

# area
gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

# export
gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MA_ha_corredor_buffer_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)



# ms ----------------------------------------------------------------------------#

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ma_mask", res = 30)

# retilineo
# overlay and
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_inside_imoveis", \
    operator = "and", overwrite = True)

# overlay not
gs.run_command("v.overlay", \
    ainput = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer", \
    binput = "suzano_properties_diss", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_outside_imoveis", \
    operator = "not", overwrite = True)

# remove columns
gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_inside_imoveis", \
    columns = ["a_cat", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])

gs.run_command("v.db.dropcolumn", \
    map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_outside_imoveis", \
    columns = ["a_cat", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_SIGLAMUNCO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA" , "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2", "a_area_ha", "b_cat", "b_OBJECTID", "b_INDCONF", "b_OBS", "b_IMOVEL", "b_SIGLAMUNLO", "b_TIPOPROPRI", "b_AREA_HA", "b_CODUNIDADE", "b_GlobalID", "b_created_us", "b_created_da", "b_last_edite", "b_last_edi_1", "b_CODMATRICU", "b_IMOVEL_ANT", "b_MATRICULA_", "b_SHAPE_STAr", "b_SHAPE_STLe", "b_NEAR_FID", "b_NEAR_DIST", "b_area", "b_area2"])


# area
gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_inside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

gs.run_command("v.to.db",\
 map = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_outside_imoveis", \
 type = "centroid", option = "area", columns = "area_ha", unit = "h")

# export
gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_inside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_inside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)

gs.run_command("v.out.ogr", \
    input = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_outside_imoveis", \
    output = "mapbiomas_2019_30m_rec_forest_suzano_null_area_MS_ha_corredor_buffer_outside_imoveis.shp", \
    format = "ESRI_Shapefile", overwrite = True)