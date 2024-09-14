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
