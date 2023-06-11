#Conversiones
"""En informática, la conversión alude al proceso de transformación de datos informáticos de una
representación concreta a otra, cambiando los bits de un formato de archivo formato a otro, normalmente
para lograr la interoperabilidad de aplicaciones o sistemas diferentes.

Los tipos de Datos son: Float(Flotante), Str(String), Int(Entero)"""

a=20
b=20
nombre="Edwin"
print(type(a))
print(type(nombre))

print("La suma es : " + str(a+b)) #Correcto
#print("La suma es : " + (a+b)) #Error

# Al realizar conversiones podemos decir que:

a = str(a)
print(type(a))

b = str(b)
print(type(b))

resultado = a+b
print("Ahora el resultado de a+b: " + resultado)