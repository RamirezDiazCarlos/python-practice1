"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

esta_lloviendo = True
riego_activado = True

# COMPLETAR - INICIO
if esta_lloviendo or riego_activado:
    print("Piso mojado")
# COMPLETAR - FIN

#assert piso_mojado

print("-------------------------------------------------------------------")
"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

# COMPLETAR - INICIO
if not(area_cuadrado < lado_cuadrado):
    print("Area mayor a 5")
# COMPLETAR - FIN

#assert area_mayor_a_cinco

print("-------------------------------------------------------------------")
"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50

# COMPLETAR - INICIO
if numero_1 % 7 == 0 and numero_2 % 7 != 0:
    print(f"El numero {numero_1} es divisible por 7, el numero {numero_2} no")
# COMPLETAR - FIN

#assert resultado

print("-------------------------------------------------------------------")
"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100

# COMPLETAR - INICIO
resultado2 = variable_01 or variable_02 and variable_03 or variable_04 or variable_05
print(resultado2)
# COMPLETAR - FIN

#assert resultado == 80