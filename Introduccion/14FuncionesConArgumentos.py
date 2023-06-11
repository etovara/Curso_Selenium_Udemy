#Funciones con Argumentos arbitrarios
"""Si no sabe cuántos argumentos se pasarán a su función, agregue un (*) antes del nombre del parámetro
 en la definición de la función. De esta manera, la función recibirá una tupla de argumentos y podrá
 acceder a los elementos en consecuencia"""

def suma (*args):
    resultado=0
    for n in args:
        resultado=resultado + n
    print("El resultado es: " + str(resultado))

suma(5,3,10,19,20)