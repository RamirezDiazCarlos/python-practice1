import sys
sys.stdout.reconfigure(encoding='utf-8')

""""Tuplas y Desempaquetado"""


"""
A partir de ls siguiente lista instanciar una tupla que contenga todos sus valores
y en el mismo orden.
"""

lista = ["casa", "perro", "pato", "gato"]

# COMPLETAR - INICIO
tupla = tuple(lista)
print(tupla)
# COMPLETAR - FIN

#assert tupla == ("casa", "perro", "pato", "gato")

print("-------------------------------------------------------------------")
"""
A partir de ls siguiente tupla instanciar una lista que contenga todos sus valores
y en el mismo orden.
"""

tupla = "casa", "perro", "pato", "gato", "tenedor"

# COMPLETAR - INICIO
lista = list(tupla)
print(lista)
# COMPLETAR - FIN

#assert lista == ["casa", "perro", "pato", "gato", "tenedor"]

print("-------------------------------------------------------------------")
"""
Desempaquetar la siguiente tupla en las variables a, b y c
"""

tupla = ("primer", 25, [1, 2, 3])

# COMPLETAR - INICIO
a, b, c = tupla
print(f"a:{a}, b:{b}, c:{c}")
# COMPLETAR - FIN

#assert a == "primer" and b == 25 and c == [1, 2, 3]

print("-------------------------------------------------------------------")
"""
Desempaquetar la siguiente tupla y luego sumar sus valores
"""

tupla = (87, 98, 35, 67, 4, 9)

# COMPLETAR - INICIO
suma = 0
for num in tupla:
    suma += num
print(f"La suma de los números de la tupla es {suma}")
# COMPLETAR - FIN

#assert total == 300

print("-------------------------------------------------------------------")
"""
Desempaquetar la siguiente lista y luego concatenar sus elementos
Restricción: Utilizar f-Strings.
"""

lista = ["esta", "mañana", "sali", "a", "correr"]

# COMPLETAR - INICIO

# COMPLETAR - FIN
frase = f"{lista[0]} {lista[1]} {lista[2]} {lista[3]} {lista[4]}"
print(frase)
#assert string_concatenado == "esta mañana sali a correr"

print("-------------------------------------------------------------------")
"""
Desempaquetar el primer elemento de la siguiente tupla
Restricción: Utilizar desempaquetado con comodines
"""

tupla = (73, 45, 344, 3434, 2)

# COMPLETAR - INICIO
x,*_ = tupla
print(f"El primer elemento de la tupla es: {x}")
# COMPLETAR - FIN

#assert primer == 73

print("-------------------------------------------------------------------")
"""
Desempaquetar el primer y el último elemento de la siguiente lista y luego sumarlos
Restricción: Utilizar desempaquetado con comodines
"""

lista = [73, 45, 344, 3434, 2]

# COMPLETAR - INICIO
a,*_,z = lista
suma = a + z
print(f"La suma del primer elemento de la lista {a} y el ultimo {z} es {suma}")
# COMPLETAR - FIN

#assert suma == 75

print("-------------------------------------------------------------------")
"""
Desempaquetar el primer, el segundo, el tercer, el cuarto y el quinto elemento de la
siguiente tupla y luego concatenarlos
Restricción: Utilizar desempaquetado con comodines y f-Strings
"""

tupla = ("anoche", "fui", "a", "la", "fiesta", "pero", "no", "pude", "entrar")

# COMPLETAR - INICIO
a, b, c, d, e, *_ = tupla
print(f"{a} {b} {c} {d} {e}")
# COMPLETAR - FIN

#assert string_concatenado == "anoche fui a la fiesta"