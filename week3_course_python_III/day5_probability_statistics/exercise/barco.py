
class Barco:

    # función constructor
    def init(self, posicion, resistencia):
        self.posicion = posicion
        self.resistencia = resistencia

    def f_no_flota(self):
        if self.resistencia <= 0:
            return True
        else:
            return False


