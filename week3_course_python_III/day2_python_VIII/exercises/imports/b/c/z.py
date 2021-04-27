import os, sys
ruta = __file__

for i in range(3):
    ruta = os.path.dirname(ruta)

sys.path.append(ruta)
import b.y as b
import a.x as a

def fz1(z):
    b.fy1(z)
fz1(7)

def fz2(z):
    a.fx2(z)
fz2(9)