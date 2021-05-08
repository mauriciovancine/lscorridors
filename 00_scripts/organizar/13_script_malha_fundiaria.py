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


# malha fundiaria ---------------------------------------------------------------- #
# directory
dir_malha = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/MalhaFundiaria_LandTenure_v.1812/union"
os.chdir(dir_malha)

# import
gs.run_command("v.import", \
    input = "rg_malhaFundiaria_landTenure_2018_imaflora_sirgas_topology_bamges.shp", \
    output = "rg_malhaFundiaria_landTenure_2018_imaflora_sirgas_topology_bamges")

gs.run_command("v.import", \
    input = "rg_malhaFundiaria_landTenure_2018_imaflora_sirgas_topology_ma.shp", \
    output = "rg_malhaFundiaria_landTenure_2018_imaflora_sirgas_topology_ma")

gs.run_command("v.import", \
    input = "rg_malhaFundiaria_landTenure_2018_imaflora_sirgas_topology_ms.shp", \
    output = "rg_malhaFundiaria_landTenure_2018_imaflora_sirgas_topology_ms")



# limites ------------------------------------------------------------------------- #
# directory
dir_li = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/unfs"
os.chdir(dir_li)

# import
gs.run_semmand("v.in.ogr", \
    input = "unf_bamges_mask_diss_gcs_sirgas2000.shp", \
    output = "unf_bamges_mask_diss_gcs_sirgas2000")

gs.run_semmand("v.in.ogr", \
    input = "unf_ma_mask_diss_gcs_sirgas2000.shp", \
    output = "unf_ma_mask_diss_gcs_sirgas2000")

gs.run_semmand("v.in.ogr", \
    input = "unf_ms_mask_diss_gcs_sirgas2000.shp", \
    output = "unf_ms_mask_diss_gcs_sirgas2000")


# overlay malha ------------------------------------------------------------------------- #
# directory
dir_malha = r"/home/mude/data/onedrive/trabalho/empresas/selecao_natural/02_corredores_suzano/02_vector/MalhaFundiaria_LandTenure_v.1812"
os.chdir(dir_malha)

# define region
gs.run_command("g.region", flags = "ap", vector = "unf_bamges_mask_diss_gcs_sirgas2000", res = "00:00:01")

# bamges overlay
gs.run_command("v.overlay", \
    ainput = "rg_se_malhaFundiaria_landTenure_2018_imaflora_sirgas", \
    binput = "unf_bamges_mask_diss_gcs_sirgas2000", \
    output = "rg_se_malhaFundiaria_landTenure_2018_imaflora_sirgas_bamges", \
    operator = "and", overwrite = True)

gs.run_command("v.overlay", \
    ainput = "rg_ne_malhaFundiaria_landTenure_2018_imaflora_sirgas", \
    binput = "unf_bamges_mask_diss_gcs_sirgas2000", \
    output = "rg_ne_malhaFundiaria_landTenure_2018_imaflora_sirgas_bamges", \
    operator = "and", overwrite = True)


# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ma_mask_diss_gcs_sirgas2000", res = "00:00:01")

# ma overlay
gs.run_command("v.overlay", \
    ainput = "rg_ne_malhaFundiaria_landTenure_2018_imaflora_sirgas", \
    binput = "unf_ma_mask_diss_gcs_sirgas2000", \
    output = "rg_ne_malhaFundiaria_landTenure_2018_imaflora_sirgas_ma", \
    operator = "and", overwrite = True)

gs.run_command("v.overlay", \
    ainput = "rg_n_malhaFundiaria_landTenure_2018_imaflora_sirgas", \
    binput = "unf_ma_mask_diss_gcs_sirgas2000", \
    output = "rg_n_malhaFundiaria_landTenure_2018_imaflora_sirgas_ma", \
    operator = "and", overwrite = True)


# define region
gs.run_command("g.region", flags = "ap", vector = "unf_ms_mask_diss_gcs_sirgas2000", res = "00:00:01")

# ms overlay
gs.run_command("v.overlay", \
    ainput = "rg_se_malhaFundiaria_landTenure_2018_imaflora_sirgas", \
    binput = "unf_ms_mask_diss_gcs_sirgas2000", \
    output = "rg_se_malhaFundiaria_landTenure_2018_imaflora_sirgas_bamges", \
    operator = "and", overwrite = True)

gs.run_command("v.overlay", \
    ainput = "rg_co_malhaFundiaria_landTenure_2018_imaflora_sirgas", \
    binput = "unf_ms_mask_diss_gcs_sirgas2000", \
    output = "rg_co_malhaFundiaria_landTenure_2018_imaflora_sirgas_bamges", \
    operator = "and", overwrite = True)


# end -------------------------------------------------------------------------- #