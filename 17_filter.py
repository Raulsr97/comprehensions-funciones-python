# La funcion filter nos ayuda a realizar un filtrado basado en una condición iterando a traves de cada uno de los elementos del iterable 
# Si ningun elemento cumple con la condicion devuelve un iterable vacío
# El valor devuelto jamás será mas grande que el original 
# No modifica el iterable filtrado si no que crea uno nuevo

numbers = [1, 2, 3, 4, 5]
new_numbers = list(filter(lambda number : number % 2 == 0, numbers ))

print(numbers)
print(new_numbers)

