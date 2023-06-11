#Ingresar Datos en una Variable
""" Con la función (Input) se puede agregar datos a una función"""

print("Cual es tu Primer Nombre")
primerNombre= input()

print("Cual es tu primer Apellido")
primerApellido= input()

print("Tu primer Nombre es: " + primerNombre)
print("Tu Primer Apellido es: "+ primerApellido)


print("Donde Vives")
direccion=input()

print("Telefono de Contacto")
telefono=input()

print("ingresa un numero: ")
a=input()
a=int(a)

print("ingresa otro numero: ")
b=input()
b=int(b)
suma=a+b

print("Tu dirección es: {} y tu telefono de contacto {} ".format(direccion,telefono))
print("La suma de: {} + {} = {}".format(a,b,suma))
