# Cada que se genera un error en la aplicacion se detiene la ejecución del programa

# Error de sintaxis:
# print(0 / 0))

# Error de división entre 0:
# print(0 / 0)

# Variable no declarada:
# print(result)

# AssertionError
# suma = lambda x, y : x + (y * 2)
# assert suma(2, 2) == 4

# Creando un error basado en una regla de negocio
age = 10
if age < 18:
    raise Exception('No se permite menores de edad')

