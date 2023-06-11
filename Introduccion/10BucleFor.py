#Bucle For
""" En general, un bucle es una estructura de control que repite un bloque de instrucciones.
Un bucle for es un bucle que repite el bloque de instrucciones un número prederminado de veces. El bloque de
instrucciones que se repite se suele llamar cuerpo del bucle y cada repetición se suele llamar iteración."""

colores=["Amarillo", "Azul", "Rojo", "Verde", "Naranja"]

for vcolor in colores:
    print(vcolor)


#Se puede hacer recorrido entre un rango determinado

for x in range(10,20):
    print(x)

#Podemos tambien realizar ese recorrido realizando incremento o condiciones especificas

for e in range(30,60,5):
    print(e)

#La declaración de ruptura (Break)
"""Con la instrucción break podemos detener el bucle antes de que haya recorrido todos los elementos"""

for num in range(0,100,7):
    if(num >= 75):
        break
    print(num)

#La declaración de continuación (Continue)
"""Con la instrucción continuar podemos detener la iteración actual del ciclo y continuar con la siguiente"""

for table in range(120,140):
    if(table==125 or table==130 or table==135):
        continue
    print(table)
