#ejercicio 3
valor_cuota = float(8000)

def descuento(a, b):
    porcentaje_a_restar = float((b*a)/100)
    return porcentaje_a_restar

aulas = {
    "par": "A-300",
    "inpar": "A-315"
}

precio_estacionamiento = {
    "auto": 300,
    "moto": 300,
    "bicicleta": 50
}

print("=============================== AULAS ==============================")
dia = float(input('Ingrese el número del dia: 1 (lunes) a 6 (sábado): '))

dia = dia/2
if dia == 1:
    print("Aula: " + aulas["par"])
else:
    print("Aula: " + aulas["inpar"])

print("=================== Documentos y estacionamiento ===================")
turno = input('Ingrese el turno: Mañana, Tarde o Noche: ')
turno = turno.lower()

materias = int(input('Ingrese la cantidad de materias: '))

if materias >= 3 and turno == "tarde":
    porcentaje_a_restar = descuento(valor_cuota, 25)
    cuota = valor_cuota - porcentaje_a_restar
    print(f"El valor de la cuota es: ${cuota}")
else:
    porcentaje_a_restar = descuento(valor_cuota, 5)
    cuota = valor_cuota - porcentaje_a_restar
    print(f"El valor de la cuota es: ${cuota}")

vehiculo = input('Ingrese el vehiculo en el que ingresa: Auto, Moto o Bicicleta: ')
vehiculo = vehiculo.lower()

if vehiculo == "auto":
    print(f"El costo de estacionamiento para Auto es: ${precio_estacionamiento[vehiculo]}")
elif vehiculo == "moto":
    print(f"El costo de estacionamiento para Moto es: ${precio_estacionamiento[vehiculo]}")
elif vehiculo == "bicicleta":
    print(f"El costo de estacionamiento para Bicicleta es: ${precio_estacionamiento[vehiculo]}")
else:
    print("Vehiculo no permitido")

