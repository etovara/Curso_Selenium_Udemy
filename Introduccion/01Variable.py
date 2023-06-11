#Variables
""" ¿Qué es una variable en programación y ejemplos?
Una variable es donde se almacenan y se recuperan los datos de un programa.
Así de simple. En programación, la utilizamos para guardar datos y estados,
asignar ciertos valores de variables a otras, representar valores de expresiones matemáticas
y mostrar valores por pantallas."""

a=10
b=20

suma = a+b
resta = a-b
multiplicacion = a*b
division = a/b


print("La suma es: " + str(suma))
print("La resta es: " + str(resta))
print("La multiplicacion es: " + str(multiplicacion))
print("La division es: " + str(division))

nombrePrimario ="Edwin"
nombreSegundario = "Manuel"
apellidoPrimario = "Tovar"
apellidoSegundario = "Aladejo"


print("Mi Nombre es: " + nombrePrimario + " " + nombreSegundario +  " " + apellidoPrimario + " " + apellidoSegundario)

#Para identificar el tipo de la variable
print(type(a))
print(type(nombrePrimario))