#Programacion Tradicional
#ejemplo entrada de datos diarios (temperaturas) y el cálculo del promedio semanal
# Programación Orientada a Objetos (POO)


class registroclima:

        def __init__(self):
            self.temperaturas = []

        def ingresar_temperaturas_diarias(self):


            for i in range(7):
                temperatura = float(input(f"Ingrese la temperatura del dia {i + 1}: "))
                self.temperaturas.append(temperatura)

        def calcular_promedio_semanal(self):

            if not self.temperaturas:
                return 0
            promedio = sum(self.temperaturas) / len(self.temperaturas)
            return promedio


def main():
    registro = registroclima()
    registro.ingresar_temperaturas_diarias()
    promedio = registro.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados ")

if __name__ == "__main__":
    main()