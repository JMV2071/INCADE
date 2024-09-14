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