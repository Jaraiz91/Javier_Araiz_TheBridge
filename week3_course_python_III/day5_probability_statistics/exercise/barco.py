class Barco:

    # función constructor
    def init(self, nombre, resistencia):
        self.nombre = nombre
        self.resistencia = resistencia

    def f_no_flota(self):
        if self.resistencia <= 0:
            return True
        else:
            return False

barco1 = Barco(nombre = "Barco1", resistencia = 2)
barco2 = Barco(nombre = "Barco2", resistencia = 2)
barco3 = Barco(nombre = "Barco3", resistencia = 2)
barco4 = Barco(nombre = "Barco4", resistencia = 2)
barco5 = Barco(nombre = "Barco5", resistencia = 3)
barco6 = Barco(nombre = "Barco6", resistencia = 3)
barco7 = Barco(nombre = "Barco7", resistencia = 3)
barco8 = Barco(nombre = "Barco8", resistencia = 4)
barco9 = Barco(nombre = "Barco9", resistencia = 4)
barco10 = Barco(nombre = "Barco10", resistencia = 5)

