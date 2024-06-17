#Programación Orientada a Objetos (POO)


class Registrotempertuarassemana:
    def __init__(self):
        self.temperaturas = []

# Método para ingresar las temperaturas diarias
    def ingresar_temperaturas_diarias(self):#
        for i in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temperatura)

#Método para calcular el promedio semanal de temperaturas
    def calcular_promedio_semanal(self):

#Retorna el promedio de las temperaturas ingresadas.

        if not self.temperaturas:
            return 0
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio

def main():
    registro = Registrotempertuarassemana()
    registro.ingresar_temperaturas_diarias()
    promedio = registro.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} ")

if __name__ == "__main__":
    main()
