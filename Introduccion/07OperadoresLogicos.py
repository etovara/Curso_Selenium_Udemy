#Operadores Logicos (AND y OR)

"""A la hora de operar con valores booleanos, tenemos a nuestra disposición los operadores and, or y not."""

"""
Operación	Resultado	                                                                Descripción
a or b	    Si a se evalúa a falso, entonces devuelve b, si no devuelve a	            Solo se evalúa el segundo operando si el primero es falso
a and b	    Si a se evalúa a falso, entonces devuelve a, si no devuelve b	            Solo se evalúa el segundo operando si el primero es verdadero
"""

a=5
b=10
c=9

a<b and a<c
print(" Si a es menor que b y a es menor que c: " + str(a<b and a<c))

a>b or a>c
print(" Si a es menor que b y a es menor que c: " + str(a>b or a>c))


