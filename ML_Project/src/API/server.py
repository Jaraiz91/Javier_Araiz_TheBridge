from flask import Flask, request, render_template
import pandas as pd
import os
import sys
import json
import argparse
from sqlalchemy import create_engine

dir = os.path.dirname
path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(path)


    # Mandatory
app = Flask(__name__)  # __name__ --> __main__  

    # ---------- Flask functions ----------

    

@app.route('/')
def enter():   
    new_path = path + os.sep + 'data' + os.sep 
    return cvs_to_json(fullpath= new_path, extension='featured_df')
    
@app.route('/sql', methods=['GET', 'POST'])
def upload():
    sql_json_readed = read_json(path + os.sep + 'src' + os.sep + 'manage_sql.json')
    IP_DNS = sql_json_readed["IP_DNS"]
    USER = sql_json_readed["USER"]
    PASSWORD = sql_json_readed["PASSWORD"]
    BD_NAME = sql_json_readed["BD_NAME"]
    PORT = sql_json_readed["PORT"]
    mysql_db = sql.MySQL(IP_DNS=IP_DNS, USER=USER, PASSWORD=PASSWORD, BD_NAME=BD_NAME, PORT=PORT)
    mysql_db.connect()
    db_connection_str = mysql_db.SQL_ALCHEMY
    db_connection = create_engine(db_connection_str)
    file_path = path + os.sep + 'data' + os.sep + 'featured_df.csv'
    panda_file = pd.read_csv(file_path)
    panda_file.to_sql(name= 'javier_araiz_miranda', con= db_connection, if_exists= 'replace', index= False)
    return 'file uploaded'








# ---------- Other functions ----------

def main():
    print("---------STARTING PROCESS---------")
    print(__file__)
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    # Para ambos: os.sep
    settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
    print(settings_file)
    # Load json from file
    json_readed = read_json(fullpath=settings_file)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    print("SERVER_RUNNING", SERVER_RUNNING)
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
            "Please, allow it to run it.")

    if __name__ == "__main__":
        main()
