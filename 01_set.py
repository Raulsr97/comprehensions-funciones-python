# Creando un set(conjunto)
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 4, 5}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tuple = set(('abc', 'def', 'ghi'))
print(set_from_tuple)

numbers = [1, 2, 3, 4, 5, 1, 2]
print(f'numbers: {numbers}')
set_numbers = set(numbers)
unique_numbers = list(set_numbers)

print(f'unique numbers: {unique_numbers}')