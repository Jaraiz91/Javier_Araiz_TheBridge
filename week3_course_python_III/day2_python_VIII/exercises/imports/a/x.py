import os, sys
ruta = __file__
for i in range(2):
    ruta = os.path.dirname(ruta)
sys.path.append(ruta)

def fx1(x):
    print(x +1)

import b.c.z as z

def fx2(x):
    z.fz2(x)
fx2(3)