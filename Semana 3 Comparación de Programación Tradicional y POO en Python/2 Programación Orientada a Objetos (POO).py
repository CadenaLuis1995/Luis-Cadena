#Programación Orientada a Objetos (POO)
#Métodos de la clase para ingresar datos y calcular el promedio semanal.

class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio(self):
        suma_temperaturas = sum(self.temperaturas)
        promedio = suma_temperaturas / len(self.temperaturas)
        return promedio

clima_semanal = ClimaSemanal()

for dia in range(7):
    temperatura = float(input(f"Ingrese la temperatura del día {dia+1}: "))
    clima_semanal.ingresar_temperatura(temperatura)

promedio_semanal = clima_semanal.calcular_promedio()

print(f"El promedio semanal del clima es: {promedio_semanal}")
