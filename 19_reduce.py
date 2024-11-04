# La función reduce() toma como argumento un conjunto de valores y lo 'reduce' a un único valor.
# Reduce tiene dos parametros(func, seq):
     # 1 Una función particular a aplicar a todos los elementos de una secuencia.
     # 2 Una secuencia de elementos
# Como funciona:
    # Primero toma los dos primeros elementos de la secuencia y aplica una función particular.
    # Toma el resultado anterior y a este valor mas el siguiente elemento de la secuencia le aplica la función particular
    # Este proceso continua hasta el último elemento del iterable.

import functools

numbers = [1, 2, 3, 4]

# def accum(counter, number):
#     print('counter = ', counter)
#     print('number = ', number)
#     return counter + number

# result = functools.reduce(accum, numbers)


result = functools.reduce(lambda counter, number : counter + number, numbers)

print(result)