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