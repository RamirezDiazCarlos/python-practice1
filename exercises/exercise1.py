"""Aritmética Básica"""


"""
Calcular el área del cuadrado usando las variables disponibles.
Restricción: Usar el operador de multiplicación
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
print(f"El area del cuadrado es: {lado_cuadrado*lado_cuadrado}")
# COMPLETAR - FIN

#assert area_cuadrado == 25

print("-------------------------------------------------------------------")
"""
Re-Escribir usando el operador de potencia.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
print(f"El area del cuadrado es: {lado_cuadrado**2}")
# COMPLETAR - FIN

#assert area_cuadrado == 25

print("-------------------------------------------------------------------")
"""
Re-Escribir usando la función pow.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
print(f"El area del cuadrado es: {pow(lado_cuadrado,2)}")
# COMPLETAR - FIN

#assert area_cuadrado == 25

print("-------------------------------------------------------------------")
"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

# COMPLETAR - INICIO
print(f"La cantidad a comprar es: {int(presupuesto_disponible/precio)}")
# COMPLETAR - FIN

#assert cantidad_a_comprar == 2

print("-------------------------------------------------------------------")
"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1

# COMPLETAR - INICIO
if numero_incalculable % 7 == 0:
    print("Es divisible por siete")
# COMPLETAR - FIN

#assert es_divisible_por_siete