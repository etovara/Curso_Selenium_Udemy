#Manejo de Cadenas
""" Permite que puedas extraer, concaternar, editar, reemplazar, realizar operaciones aritmeticas, a traves
 de las cadenas de caracteres (String) dentro de una funcion o una variable"""

texto="Hola Bienvenido a python"

print(texto)
print(texto[3])
print(texto[5:15])
print(texto[5:])
print(texto[-6:])


#Concatenar
mensaje1 = 'Hola' + ' ' + 'Mundo'
print(mensaje1)

#Multiplicar
mensaje2a = 'Hola ' * 3
mensaje2b = 'Mundo'
print(mensaje2a + mensaje2b)

#Añadir
mensaje3 = 'Hola'
mensaje3 += ' '
mensaje3 += 'Mundo'
print(mensaje3)

#Extensiones
"""Puedes determinar el número de caracteres en una cadena utilizando el método len. 
Acuérdate que los espacios en blanco cuentan como un carácter."""

mensaje4 = 'hola' + ' ' + 'mundo'
print(len(mensaje4))

#Encontrar
"""Puedes buscar una sub-cadena en una cadena de caracteres utilizando el método find y tu programa te 
indicará el índice de inicio de la misma.Ten en mente que los índices están numerados de izquierda a 
derecha y que el número en el que se comienza a contar la posición es el 0, no el 1."""

mensaje5 = "Hola Mundo"
mensaje5a = mensaje5.find("Mundo")
print(mensaje5a)
#Si la sub-cadena no está presente el programa imprimirá el valor -1.
mensaje6 = "Hola Mundo"
mensaje6a = mensaje6.find("ardilla")
print(mensaje6a)


#Reemplazar
"""Si necesitas cambiar una sub-cadena de una cadena se puede utilizar el método replace"""

mensaje8 = "HOLA MUNDO"
mensaje8a = mensaje8.replace("L", "pizza")
print(mensaje8a)


#Minúsculas y Mayuscula
"""A veces es útil convertir una cadena de caracteres a minúsculas o mayusucla. 
Para ello se utiliza el método lower (miniscula) upper (mayuscula)."""

mensaje7 = "HOLA MUNDO"
mensaje7a = mensaje7.lower()
print(mensaje7a)

mensaje7b = "hola mundo"
mensaje7c = mensaje7b.upper()
print(mensaje7c)


#Separador de Cadena
""" El metodo (split) permite separar a traves de una coma una cadena de caracteres en forma de lista"""

cadena="php,java,selenium,python,java,javascript"
print(cadena.split(','))
