r.colors map=mapbiomas_30m@PERMANENT color=viridis
v.colors map=mapbiomas_30m_diss@PERMANENT use=cat color=viridis
g.remove -f type=vector name=mapbiomas_30m_diss@PERMANENT
g.remove -f type=vector name=mapbiomas_30m_diss@PERMANENT,mapbiomas_30m@PERMANENT
v.colors map=source_target@PERMANENT use=cat color=viridis
v.colors map=source_target@PERMANENT use=cat column=cat color=viridis
# iniciar o python
python3
cd /home/mude/data/github/lscorridors/lscorridors
python LS_corridors_v1_0_3.py
python LS_corridors_v1_0_4.py
python r_ls_corridors_v1_0_4.py
python3
ls
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
# iniciar o python
python3
ls
# iniciar o python
python3
cd /home/mude/data/github/lscorridors/lscorridors
python3 LS_corridors_v1_0_4.py
g.list rast
