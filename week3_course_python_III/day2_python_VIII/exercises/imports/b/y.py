
import os, sys

ruta = __file__
for i in range(2):
    ruta = os.path.dirname(ruta)
print("-------+++-----")
print(sys.path)
sys.path.append(ruta)
print("--------------")
print(sys.path)
import a.x as a

def fy1(x):
    a.fx1(x)
fy1(3)

def fy2(y):
    a.fx2(y)
fy2(6)
