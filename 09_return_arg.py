# Asignando un valor por defecto a los parametros
def find_volume(lenght=1, width=1, depth=1):
    # Haciendo multiples retornos
    return lenght * width * depth, width, 'hola'

print(find_volume())
print(find_volume(lenght=20))

result = find_volume(2, 3, 4)
print(result)