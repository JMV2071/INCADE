#ejercicio 1

nombre = input('ingrese su nombre y apellido: ')
edad = input('ingrese su edad: ')
nacimiento = input('ingrese fecha de nacimiento (DD/MM/AAAA): ')
matricula = float(input('ingrese el monto de la matricula: ')) 
titulo = str(True)
cuota = float((matricula + 1000)) 
PythonI_xmes = float(12000/4)
PythonI_xmes_descuento = float((12000 - ((15*12000)/100))/4)

print("===============================================")
print("============UNIVERSIDAD DE PYTHON==============")
print("===============================================")

print("DATOS DE INGRESO: ")
print("Nombre completo: " + nombre)
print("Fecha de nacimiento y edad: "+ nacimiento + " (" + edad + ")")
print("Posee titulo secundario?: " + titulo)
print("Matricula: " + str(matricula))
print("Cuota: " + str(cuota))
print("Arancel mensual materia 'Python I': $" + str(PythonI_xmes))
print("Arancel mensual materia 'Python I' con descuento: $" + str(PythonI_xmes_descuento))

#ejercicio 2
print("=====================================")
print("==========notas de examenes==========")
print("=====================================")

par1 = float(input('Ingrese la nota del primer parcial: '))
par2 = float(input('Ingrese la nota del segundo parcial: '))

prom = str((par1 + par2)/2)
print("el promedio de las notas es: " + prom)

if par2 >= 7:
    print("Aprobó el segundo parcial")
else:
    print("Desaprobó el segundo parcial")

if par1 == par2:
    print("Progreso del 1er al 2do parcial: mantuvo su desempeño")
elif par1 > par2:
    print("Progreso del 1er al segundo parcial: empeoró su desempeño")
elif par1< par2:
    print("Progreso del 1er al 2do parcial: mejoró su desempeño")
else:
    print ("error")

prom = float(prom)

if prom >= 7:
    print("Promocionó la materia")
else:
    if prom >=4:
        print("Debe rendir exámen final")
    else:
        print("Debe recursar la materia")

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

#ejercicio 4

Aulas = {
    1 : "A-315",
    2 : "A-300",
    3 : "A-315",
    4 : "A-300",
    5 : "A-315",
    6 : "A-300"
}

print("=============== Listado de aulas ===============")
print("Dia     Aula")
for i in range(6):
    i = i+1
    print(f"{i}     {Aulas[i]}")

print("=============== Carga de edades ===============")
salir = False
edad_erronea = 0

while salir==False:
    edad = int(input('Ingrese una edad mayor o igual a 18: '))
    if edad>=18:
        salir = True
    else:
        edad_erronea = edad_erronea+1

print(f"La edad ingresada es: {edad}")
print(f"Se ha ingresado la edad erroneamente {edad_erronea} veces")

print("=============== Promedio de notas ===============")
sum = float(0)
for i in range(5):
    nota = float(input('Ingrese la nota: '))
    sum = sum + nota
prom = sum/5
print(f"El promedio de notas es de: {prom}")

print("=============== Costos del comedor ===============")
print("Dia     Costo")
costo = int(0)
for e in range(6):
    e = e+1
    costo = costo + 1250
    print(f"{e}     {costo}")