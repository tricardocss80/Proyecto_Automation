class Automovil():
    def __init__(self,color,marca,velocidad_maxima):
        self.color = color
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def mostrar_velocimetro(self):
        print('La velocidad actual es de ' +str(self.velocidad_actual) + 'de ' +str(self.velocidad_maxima))

    def aceler(self,velocidad):
        self.velocidad_actual = self.velocidad_actual + velocidad

    def frenar(self,velocidad):
        self.frenar = self.velocidad_actual - self.velocidad_actual - velocidad


mi_auto = Automovil('verde','Peugeot', 180)
print(mi_auto.color)
print(mi_auto.marca)
mi_auto.mostrar_velocimetro()
mi_auto.aceler(80)
mi_auto.mostrar_velocimetro()
mi_auto.aceler(20)
mi_auto.frenar(50)
mi_auto.mostrar_velocimetro()