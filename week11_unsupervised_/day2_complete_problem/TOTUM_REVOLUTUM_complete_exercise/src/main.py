"""
Siempre que veas 'pass' es un TO-DO (por hacer)

"""

"""1"""
# Llama a la función 'mi_funcion' que está en /flask/api.py. No puede dar error.
import sys, os
path  = os.path.abspath(__file__)
path = os.path.dirname(path)
path = path + os.sep + 'flask'
sys.path.append(path)

import api

api.mi_funcion()