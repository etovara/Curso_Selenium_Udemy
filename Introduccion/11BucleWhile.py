#El ciclo while (While)
"""Con el bucle while podemos ejecutar un conjunto de declaraciones siempre que una condición sea verdadera."""

inicio=1
fin=10

while(inicio <= fin):
    print("Esto se repite" + str(inicio))
    inicio = inicio + 1

# Si aplicamos el bucle Break podemos indicar que se detenga en X valor.

primero=20
ultimo=30

while(primero <= ultimo):
    print("Aca se detiene" + str(primero))
    primero = primero + 2
    if (primero==26):
        break

# Si aplicamos el bucle continue podemos indicar que se detenga en un punto especifico y continue la acción.

primeroInicia=40
ultimoCulminar=65

while(primeroInicia <= ultimoCulminar):
    primeroInicia = primeroInicia + 2
    if (primeroInicia==56):
        continue
    print("Aca se detiene" + str(primeroInicia))