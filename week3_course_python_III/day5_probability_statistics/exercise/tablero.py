import numpy as np
class Tablero:
    def __init__ (self, name):
        pdefensa = [[["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10]]
        pataque = [[["o"]*10],[["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10]] 
        resistencia = 10
        flota = {}

        self.ataque = pataque
        self.defensa = pdefensa
        self.name = name
        self.flota = flota
        self.resistencia = resistencia
    def mostrar_defensa(self):
        for x in self.defensa:
            print(x)

    def mostrar_ataque(self):
        for x in self.ataque:
            print(x)

    def colocar(self, coordenada):
        renglon = []
        orient = ""
        casillas = []
        inicio = []
        fin = []
        for i, val in enumerate(coordenada):
            if val == "v" or val == "h":
                renglon.append(coordenada[:i])
                orient = val
                casillas.append(coordenada[i+1:])
        casillas2 = casillas[0]
        for i,x in enumerate(casillas2):
            if x == ":":
                inicio.append(casillas2[:i])
                fin.append(casillas2[i+1:])
        renglon = int("".join(renglon))
        casillas = "".join(casillas)
        inicio = int("".join(inicio)) 
        fin = int("".join(fin)) 
        if orient == "v":
            contador = inicio - 1
            while contador < fin :
                if self.defensa[contador][0][renglon -1] == "#":
                    return False
                else:
                    self.defensa[contador][0][renglon -1] = "#"
                    contador += 1
        elif orient == "h":
            contador = inicio - 1
            while contador < fin:
                self.defensa[renglon - 1][0][contador] = "#"
                contador += 1

    
    def quitar_vida(self, casilla):
        for key, val in self.flota.items():
            if casilla in val:
                for i, k in enumerate(val):
                    if k == casilla:
                        val.remove(k)
                        if len(val) == 0:
                            self.resistencia -=1
                            return True

  
