
import os, sys

ruta = __file__
print(ruta)
print("------------------")
print(os.path.dirname(ruta))
para_path= os.path.dirname(os.path.dirname(ruta))
sys.path.append(para_path)
from a.x as a

def fy1(x):
    print(a.fx1(x))

fy1(6)
