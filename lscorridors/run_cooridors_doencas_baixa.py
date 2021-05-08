# bernardo niebuhr
# 2019-06-11

# open Python
python

# import modules
import os, fnmatch, imp
import subprocess
import grass.script as grass
from grass.pygrass.modules.shortcuts import general as g
from grass.pygrass.modules.shortcuts import vector as v
from grass.pygrass.modules.shortcuts import raster as r

# import limits
di = r'D:\lactec_corredores\02_input\limits/'
os.chdir(di)

v.in_ogr(input = 'Bacia_Doce_buffer30km_costa_albers_sirgas2000.gpkg', output = 'Bacia_Doce_buffer30km_costa_albers_sirgas2000')
v.in_ogr(input = 'limite_mapeado_compartimentos_albers_SIRGAS2000.shp', output = 'limite_mapeado_compartimentos_albers_SIRGAS2000')
v.in_ogr(input = 'SUBCOMP_AREA_AMBIENTAL1_albers_sirgas.gpkg', output = 'SUBCOMP_AREA_AMBIENTAL1_albers_sirgas')

# import sts
di = r'D:\lactec_corredores\02_input\sts'
os.chdir(di)

r.in_gdal(input = 'sts_code_raster.tif', output = 'sts_code_raster')

# import resistance maps
di = r'\lactec_corredores\02_input\resistancesurfaces'
os.chdir(di)

files = os.listdir('.')
for i in files:
    if i.endswith('.tif') and 'doencas_baixa' in i:
        name = i.replace('.tif', '')
        r.in_gdal(input = i, output = name)

# run lscorridors
di = r'D:\lactec_corredores\01_code\LS_CORRIDORS\_LS_Corridors_v1_0_1_doencas_baixa'
os.chdir(di)

# through LSCorridors GUI
#subprocess.call('python LS_corridors_v1_0_2.py', shell=True) # runs and wait

# trough command line

# Import modules
r_ls_corridors = imp.load_source('main', 'r.ls.corridors.py')

# species
sp = ['doencas_baixa_aedes_scapularis']

# all resistance maps
maps_all = grass.list_grouped(type = 'raster', pattern = 'resist*')['PERMANENT']

# output folder
outdir = r'D:\lactec_corredores\03_output'

# for each species
for i in sp:
    
    # create folder
    dir_path = outdir + '/' + i
    try:
        os.mkdir(dir_path)
    except:
        print 'The folder ' + dir_path + ' already exists!'
    
    # subset of maps
    print i
    
    # maps for each species
    maps = [j for j in maps_all if i in j]
    
    # st map
    st = 'sts_code_raster'
    
    # ST pairs to be connected
    pairs = '121,111,122,112,123,113,124,114,125,115,126,116,211,212,212,213,213,214,221,222,222,223,223,224'
    
    # Iterate from i = 0 to i = 2
    for mm in range(len(maps)):
        
        resist = maps[mm]
        out_name = resist.replace('resist', 'corridors')
        print out_name
        
        # Run corridors
        di = r'D:\lactec_corredores\01_code\LS_CORRIDORS\_LS_Corridors_v1_0_1_doencas_baixa'
        os.chdir(di)
        
        r_ls_corridors.main(resistancemap = resist, stmap = st, stlist = pairs, output_prefix = '', 
                            output_folder = dir_path, variability = '2.0', scale = '100', 
                            simulations = '20', method = 'MP')