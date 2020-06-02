class Automovil():
    def __init__(self, color, marca, velocidad_maxima):
        self.color = color
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def mostrar_velocimetro(self):
        print("La velocidad actual es " + str(self.velocidad_actual) + " de " + str(self.velocidad_maxima))

    def acelerar(self, velocidad):
        if self.velocidad_actual + velocidad > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
        else:
            self.velocidad_actual = self.velocidad_actual + velocidad
        self.mostrar_velocimetro()

    def frenar(self,velocidad):
        if self.velocidad_actual - velocidad < 0:
            self.velocidad_actual = 0
        else:
            self.velocidad_actual = self.velocidad_actual - velocidad
        self.mostrar_velocimetro()


mi_auto = Automovil('verde', 'Peugeot', 180)
print(mi_auto.color)
print(mi_auto.marca)

mi_auto.acelerar(200)
mi_auto.acelerar(170)
mi_auto.frenar(5000)
