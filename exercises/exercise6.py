import sys
sys.stdout.reconfigure(encoding='utf-8')

"""Listas"""

"""
Inicializar una lista vacía y luego agregarle 4 elementos cualquiera
Restricción: Utilizar el método append
"""

# COMPLETAR - INICIO
lista_01 = []
lista_01.append(1)
lista_01.append(2)
lista_01.append(3)
lista_01.append(4)
print(len(lista_01))
# COMPLETAR - FIN

#assert len(lista_01) == 4

print("-------------------------------------------------------------------")
"""
Extraer el cuarto elemento de la lista
Restricción: Utilizar el método pop
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

# COMPLETAR - INICIO
print(f"El elemento extraido es {lista.pop(3)}")
# COMPLETAR - FIN

#assert elemento_extraido == 6

print("-------------------------------------------------------------------")
"""
Concatenar las siguientes listas
Restricción: Utilizar el método extend
"""

lista_a = [1, 2, 3]
lista_b = ["4", "5", "6"]
lista_c = ["siete", "ocho", "nueve"]

# COMPLETAR - INICIO
for x in lista_b:
    lista_a.append(x)
for x in lista_c:
    lista_a.append(x)
print(lista_a)
# COMPLETAR - FIN

#assert listas_concatenadas_01 == [1, 2, 3, "4", "5", "6", "siete", "ocho", "nueve"]

print("-------------------------------------------------------------------")
"""
Agregar la variable variable_01 en la tercer posición de la lista lista_nueva
Restricción: Utilizar el método insert
"""

variable_01 = 2
lista_nueva = [0, 1, 3, 4]

# COMPLETAR - INICIO
lista_nueva.insert(2, variable_01)
print(lista_nueva)
# COMPLETAR - FIN

#assert lista_nueva == [0, 1, 2, 3, 4]

print("-------------------------------------------------------------------")
"""
Armar una lista que contenga el primer y el último elemento de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, 42, 81, 6, "la"]

# COMPLETAR - INICIO
x = []
x.append(lista[0])
x.append(lista[-1])
print(x)
# COMPLETAR - FIN

#assert lista_primero_y_ultimo == ["ho", "la"]

print("-------------------------------------------------------------------")
"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

# COMPLETAR - INICIO
x = []
x.append(lista[0])
x.append(lista[1])
x.append(lista[2])
print(x)
# COMPLETAR - FIN

#assert lista_primeros == ["ho", 3.1416, "la"]

print("-------------------------------------------------------------------")
"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar indexado múltiple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

# COMPLETAR - INICIO
x = lista[:3]
print(x)
# COMPLETAR - FIN

#assert lista_primeros == ["ho", 3.1416, "la"]

print("-------------------------------------------------------------------")
"""
Armar una lista que contenga los primeros 2 y los últimos 2 elementos de la
siguiente lista
Restricción: Utilizar el método extend junto al indexado múltiple
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

# COMPLETAR - INICIO
z = []
z.extend(lista[:2])
z.extend(lista[-2:])
print(z)
# COMPLETAR - FIN

#assert lista_primeros_y_ultimos == ["ho", "la", "como", "estas?"]

print("-------------------------------------------------------------------")
"""
Concatenar las siguientes 2 listas
Restricción: Utiliar el operador +
"""

lista_01 = [0, 1, 2, 3]
lista_02 = [5, 6]

# COMPLETAR - INICIO
y = [lista_01 + lista_02]
print(y)
# COMPLETAR - FIN

#assert lista_concatenada == [0, 1, 2, 3, 5, 6]

print("-------------------------------------------------------------------")
"""
Concatenar 3 veces la siguiente lisa consigo misma
Restricción: Utiliar el operador *
"""

lista_01 = [0, 1, 0, 1, 0, 1]

# COMPLETAR - INICIO
c = lista_01*3
print(c)
# COMPLETAR - FIN

#assert lista_duplicada == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

print("-------------------------------------------------------------------")
"""
Verificar si el siguiente elemento pertenece a la lista
Restricción: Utiliar el operador in
"""

elemento = 1.0
lista = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1.0, 1, 0, 1, 0, 1]

# COMPLETAR - INICIO
if elemento in lista:
    print(f"El elemento {elemento} se encuentra en la lista")
# COMPLETAR - FIN

#assert variable_booleana

print("-------------------------------------------------------------------")
"""
Verificar si las siguientes listas son iguales
Restricción: Utilizar el operador ==
"""

lista_01 = [1, 2, 3, 4.5, 6, 7]
lista_02 = [1, 3, 2, 4, 5, 6, 7]

# COMPLETAR - INICIO
if lista_01 == lista_02:
    print("Las listas son iguales")
else:
    print("Las listas no son iguales")
# COMPLETAR - FIN

#assert not son_iguales

print("-------------------------------------------------------------------")
"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno no tiene examenes aprobados.
Restricción: Utilizar el método any
"""

notas = [False, False, False, False, False, False, False, False, False]

# COMPLETAR - INICIO
if any(notas) == False:
    print("El alumno no tiene exámenes probados")
# COMPLETAR - FIN

#assert no_tiene_examenes_aprobados

print("-------------------------------------------------------------------")
"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno ha aprobado todos sus exámenes.
Restricción: Utilizar el método all
"""

notas = [True, True, False, True, True, True, True, True, True, True, True, True]

# COMPLETAR - INICIO
if all(notas) == True:
    print("Tiene todo aprobado")
else:
    print("No tiene todo aprobado")
# COMPLETAR - FIN

#assert not tiene_todo_aprobado