#Funciones con Parametros
""" Puedes definir valores predeterminados para los parámetros, de esa manera Python interpretará
 que el valor de ese parámetro es el predeterminado si no se proporciona ninguno."""

def saludar():
    print("Hola como estas")

def salir():
    print("Hasta Luego")

def sumar(a,b):
    resultado=a+b
    print("La suma es: " + str(resultado))

saludar()
sumar(10,15)
salir()


# Otra manera de realizar una funcion que pase parametros es:

def datos(nom,apell,apmater):
    print("Tu nombre es: {} {} {}" .format(nom,apell,apmater))

datos("Edwin","Tovar","Aladejo")