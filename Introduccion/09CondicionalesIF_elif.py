#Condicionales
""""Estas construcciones permiten condicionar la ejecución de uno o varios bloques de sentencias al
cumplimiento de una o varias condiciones."""

#La estructura de control if ... permite que un programa ejecute unas instrucciones cuando se cumplan
# una condición. En inglés "if" significa "si" (condición).



a=5
b=10
d=2
e=8

if(a>b):
    print("El valor Mayor es a: " + str(a))
else:
    print("En caso contrario el mayor es b: "+ str(b))

if(d<e):
    print("El valor Mayor es a: " + str(d))
else:
    print("En caso contrario el mayor es b: "+ str(e))

nombre="Alberto"

if (nombre=="Juan"):
    print("Tu Nombre es: " + nombre)
else:
    print("Tu no eres Juan")

#_______________________________________________________________________________________________________

#elif
"""La palabra clave elif es la forma en que Python dice 
"si las condiciones anteriores no fueron ciertas, intente con esta condición"."""

a=5
b=10
c=2

if (a>b and a>c):
    print("El Mayor es: " + str(a))
elif (b>a and b>c):
    print("El Mayor es: " + str(b))

if (a>b or a>c):
    print("El Mayor es: " + str(a))
elif (b>a or b>c):
    print("El Mayor es: " + str(b))


