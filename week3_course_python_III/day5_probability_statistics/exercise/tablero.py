import numpy as np
class tablero:
    def __init__(self, defensa = [[["o"]*10],[["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]
    *10], [["o"] * 10], [["o"] * 10], [["o"] * 10], [["o"]* 10]], ataque = [[["o"]*10],[["o"]*10], [["o"]*10], [["o"]*10], [["o"]*10], [["o"]
    *10], [["o"] * 10], [["o"] * 10], [["o"] * 10], [["o"]* 10]]):
        self.ataque = ataque
        self.defensa = defensa
    def mostrar_ataque(self):
        for x in self.ataque:
            print(x)
    def mostrar_defensa(self):
        for x in self.defensa:
            print(x)
    

