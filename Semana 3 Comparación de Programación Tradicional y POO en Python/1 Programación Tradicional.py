#Programacion Tradicional
#ejemplo entrada de datos diarios (temperaturas) y el cálculo del promedio semanal
# Programación Orientada a Objetos (POO)

def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {dia+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio(temperaturas):
    suma_temperaturas = sum(temperaturas)
    promedio = suma_temperaturas / len(temperaturas)
    return promedio

temperaturas_semana = ingresar_temperaturas()
promedio_semanal = calcular_promedio(temperaturas_semana)

print(f"El promedio semanal del clima es: {promedio_semanal}")
