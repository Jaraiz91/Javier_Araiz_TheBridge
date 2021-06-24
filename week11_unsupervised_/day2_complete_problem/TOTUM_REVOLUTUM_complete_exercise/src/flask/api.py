"""

Crea una API flask con un solo endpoint que muestre por pantalla el json 'googleplaystore.json'
de la carpeta /data. En resumen, el endpoint tiene que leer el fichero 'googleplaystore.json' y retornarlo.

Además, este fichero contiene otra función que está fuera de la funcionalidad de la API flask

"""

""" 1: No es una función de flask"""
from flask import Flask, request, render_template
import os
import sys
import json
import os, sys
import json

def mi_funcion():
    route = os.path.abspath(__file__)
    for i in range(2):
        route = os.path.dirname(route)
    sys.path.append(route)

    from utils.flask_functions import funcion_flask_1

    return funcion_flask_1()
    """
    TODO - Esta función ha de llamar a la función 'funcion_flask_1' que está en /utils/flask_functions.py y
    mostrar por pantalla lo que retorne esa función. 
    """
    pass



# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------

# localhost:6060/give_me_id?password=12345
@app.route('/')
def home():
    route = os.path.abspath(__file__)
    for i in range(3):
        route = os.path.dirname(route)
    sys.path.append(route)
    with open(route +os.sep + 'data' + os.sep + 'googleplaystore.json', 'r+') as outfile:
        json_readed = json.load(outfile)
    return json_readed



# ---------- Other functions ----------



if __name__ == "__main__":
    def main():
        route = os.path.abspath(__file__)
        for i in range(3):
            route = os.path.dirname(route)
        sys.path.append(route)
        
        with open (route + os.sep + 'config' + os.sep + 'flask_settings.json', 'r+') as outfile:
            json_readed = json.load(outfile)
        
        SERVER_RUNNING = json_readed["server_running"]
        
        if SERVER_RUNNING:
            DEBUG = json_readed["debug"]
            HOST = json_readed["host"]
            PORT_NUM = json_readed["port"]
            app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    main()
    



""" PARTE PURA DE FLASK """



""" Todo lo que está aquí debajo tiene que ver con la funcionalidad del flask """

"""2"""
  