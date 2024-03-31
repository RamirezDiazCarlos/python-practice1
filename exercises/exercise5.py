import sys
sys.stdout.reconfigure(encoding='utf-8')
"""Strings"""


"""
Formatear las siguientes variables de tipo string en un único string.
Restricción: Utilizar el operador +.
"""

variable_01 = "¡Buenos "
variable_02 = "días "
variable_03 = "a todos!"

# COMPLETAR - INICIO
frase = variable_01 + variable_02 + variable_03
print(frase)
# COMPLETAR - FIN

#assert strings_concatenados == "¡Buenos días a todos!"

print("-------------------------------------------------------------------")
"""
Formatear los siguientes strings en un único string.
Restricción: Usar directamente los strings y la concatenación automática (no
usar operadores).
"""

"¡Mamá "
"estoy concatenando "
"strings!"

# COMPLETAR - INICIO
frase = "¡Mamá " "estoy concatenando " "strings!"
print(frase)
# COMPLETAR - FIN

#assert strings_concatenados == "¡Mamá estoy concatenando strings!"

print("-------------------------------------------------------------------")
"""
Formatear las siguientes variables en un único string.
Aclaración: Se debe convertir la variable entera a string
Restricción: Utilizar el operador +.
"""

variable_01 = "Le debo "
variable_02 = 600
variable_03 = " pesos a un amigo."

# COMPLETAR - INICIO
frase = variable_01 + str(variable_02) + variable_03
print(frase)
# COMPLETAR - FIN

#assert strings_concatenados == "Le debo 600 pesos a un amigo."

print("-------------------------------------------------------------------")
"""
Formatear las siguientes variables en un único string.
Aclaración: No es necesario realizar conversiones de tipo.
Restricción: Utilizar el método format.
"""

variable_01 = "Le debo"
variable_02 = 6
variable_03 = "pesos a un amigo hace"
variable_04 = "años."
variable_05 = "Se llama Ezequiel"

# COMPLETAR - INICIO
print("{} {} {} {} {}".format(variable_01, variable_02, variable_03, variable_04, variable_05))
# COMPLETAR - FIN

#assert (    strings_concatenados == "Le debo 6 pesos a un amigo hace 6 años. Se llama Ezequiel")

print("-------------------------------------------------------------------")
"""
Formatear las siguientes variables en un único string.
Restricción: Utilizar f-Strings.
"""

variable_01 = "Le pagué "
variable_02 = 2
variable_03 = " pesos que le debía a Ezequiel, me faltan $"
variable_04 = 4

# COMPLETAR - INICIO
print(f"{variable_01}{variable_02}{variable_03}{variable_04}")
# COMPLETAR - FIN

#assert strings_concatenados == "Le pagué 2 pesos que le debía a Ezequiel, me faltan $4"