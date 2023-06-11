#Listas
"""Las listas en Python son un tipo contenedor, compuesto, que se usan para almacenar conjuntos de
elementos relacionados del mismo tipo o de tipos distintos."""

lenguaje=["php", "Java", "Pyhton", "Java", "JavaScript", "Selenium"]
print("Lenguaje Seleccionado: " + lenguaje[2])

lenguaje[2]="Djgango"
print("Nuevo Lenguaje Seleccionado: " + lenguaje[2])

#Agregar Valores a la Lista
"""Para añadir un nuevo elemento a una lista se utiliza el método append() y 
para añadir varios elementos, el método extend():"""

lenguaje.append("Groovy")
print(lenguaje)

lenguaje.extend(["Html", "Ccs", "Kotllin"])
print(lenguaje)

#Remover Valores a la Lista
"""Podemos usar los métodos remove() y pop([i]). remove() elimina la primera ocurrencia que se encuentre
 del elemento en una lista. Por su parte, pop([i]) obtiene el elemento cuyo índice sea igual a i y lo 
 elimina de la lista. Si no se especifica ningún índice, recupera y elimina el último elemento."""

lenguaje.remove("Html")
print(lenguaje)