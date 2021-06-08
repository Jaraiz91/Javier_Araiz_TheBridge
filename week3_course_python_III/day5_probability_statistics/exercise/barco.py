
class Barco:

    # función constructor
    def init(self, posicion, resistencia):
        self.posicion = posicion
        self.resistencia = resistencia
    
    def quitar_vida(self, casilla):
        for key, val in self.posicion.items():
            if [10,6] in val:
                for i, k in enumerate(val):
                    if k == [10,6]:
                        val.remove(k)
                    if len(val) == 0:
                        print("barco hundido")
        self.resistencia -=1

    def f_no_flota(self):
        if self.resistencia <= 0:
            return True
        else:
            return False


