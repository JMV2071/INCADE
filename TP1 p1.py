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