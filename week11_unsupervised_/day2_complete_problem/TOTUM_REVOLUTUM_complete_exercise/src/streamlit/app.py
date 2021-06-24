import streamlit as st
from PIL import Image
import os, sys
import pandas as pd
import json

@st.cache
def pull_data():
    sql_path = dir(path) + os.sep + "config" + os.sep + "bd_info.json"

    with open(sql_path, "r") as json_file:
        read_json = json.load(json_file)

    IP_DNS = read_json["IP_DNS"]
    PORT = read_json["PORT"]
    USER = read_json["USER"]
    PASSWORD = read_json["PASSWORD"]
    BD_NAME = read_json["BD_NAME"]

    sql = sq.MySQL(IP_DNS, USER, PASSWORD, BD_NAME, PORT)

    sql.connect()

    select_sql = """SELECT * FROM fire_nrt_M6_96619"""
    #select_sql = '''
    #SELECT * FROM fire_archive_M6_96619
    #UNION
    #SELECT * FROM fire_archive_V1_96617
    #ORDER BY City;'''

    result = sql.execute_get_sql(select_sql)
    df = pd.DataFrame(result)

    return df

df = pull_data()


""" Siempre que veas 'pass' es un TO-DO (por hacer)"""

"""1"""
# Haz que se pueda importar correctamente estas funciones que están en la carpeta utils/

def open_route(steps):
    route = os.path.abspath(__file__)
    for i in range(steps):
        route = os.path.dirname(route)
    sys.path.append(route)
    return route

open_route(2)

from utils.stream_config import draw_map
from utils.dataframes import load_csv_for_map
menu = st.sidebar.selectbox('Menu:',
            options=["No selected", "Load Image", "Map", "API", "MySQL", "Machine Learning"])

if menu == "No selected": 
    """2"""
    # Pon el título del proyecto que está en el archivo "config.json" en /config
    with open(open_route(3) + os.sep + 'config' + os.sep + 'config.json', 'r+') as outfile:
        json_loaded = json.load(outfile)

    st.title(json_loaded['Title'])
    # Pon la descripción del proyecto que está en el archivo "config.json" en /config
    st.write(json_loaded['Description'])
    
if menu == "Load Image": 
    """3"""
    # Carga la imagen que está en data/img/happy.jpg
    image = Image.open(open_route(3) + os.sep + 'data' + os.sep + 'img' + os.sep + 'happy.jpg')  
    st.image (image,use_column_width=True)

if menu == "Map":
    """4"""
    # El archivo que está en data/ con nombre 'red_recarga_acceso_publico_2021.csv'
    csv_map_path = open_route(3) + os.sep + 'data' + os.sep + 'red_recarga_acceso_publico_2021.csv'
    df_map = load_csv_for_map(csv_map_path)
    draw_map(df_map)

if menu == "API":

    st.table(pd.read_json('http://127.0.0.1:6060/'))
    """5"""
    # Accede al único endpoint de tu API flask y lo muestra por pantalla como tabla/dataframe
    pass

if menu == "MySQL":

    open_route(2)
    from utils import sql_functions as s
    from sqlalchemy import create_engine
    with open(open_route(3) + os.sep + 'config' + os.sep + 'bd_info.json', 'r+') as outfile:
        json_readed = json.load(outfile)
    
    IP_DNS = json_readed["IP_DNS"]
    USER = json_readed["USER"]
    PASSWORD = json_readed["PASSWORD"]
    BD_NAME = json_readed["BD_NAME"]
    PORT = json_readed["PORT"]

    mysql_db = s.MySQL(IP_DNS=IP_DNS, USER=USER, PASSWORD=PASSWORD, BD_NAME=BD_NAME, PORT=PORT)
    mysql_db.connect()


    select_sql = """SELECT * FROM fire_archive_M6_96619"""
                    #UNION
                    #SELECT * FROM fire_archive_V1_96617"""
    result = mysql_db.execute_get_sql(select_sql)
    df = pd.DataFrame(result)
    st.table(df.head())

if menu == "Machine Learning":
    open_route(2)
    from utils import ml
    ml.mlear(df)






    """6"""

    # 1. Conecta a la BBDD
    # 2. Obtén, a partir de sentencias SQL (no pandas), la información de las tablas que empiezan por 'fire_archive*' (join)
    # 3. Entrena tres modelos de ML diferentes siendo el target la columna 'fire_type'. Utiliza un pipeline que preprocese los datos con PCA. Usa Gridsearch.  
    # 4. Añade una entrada en la tabla 'student_findings' por cada uno de los tres modelos. 'student_id' es EL-ID-DE-TU-GRUPO.
    # 5. Obtén la información de la tabla 'fire_nrt_M6_96619' y utiliza el mejor modelo para predecir la columna target de esos datos. 
    # 6. Usando SQL (no pandas) añade una columna nueva en la tabla 'fire_nrt_M6_96619' con el nombre 'fire_type_EL-ID-DE-TU-GRUPO'
    # 7. Muestra por pantalla en Streamlit la tabla completa (X e y)
    pass



