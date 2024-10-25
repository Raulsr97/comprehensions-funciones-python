set_countries = {'col', 'mex', 'bol'}

#Obtener el tamaño de un conjunto
size = len(set_countries)
print(size)

#Obtener si un elemento esta dentro del atributo
print('mex' in set_countries)

#Agregar un elemento al conjunto add()
set_countries.add('ven')
print(set_countries)

# Actualizar un conjunto update()

set_countries.update({'arg', 'per'})
print(set_countries)

# Eliminar elemento y  si no existe lanza un error
set_countries.remove('col')
print(set_countries)

# Elimina un elemento y si ya existe no lanza ninugn error
set_countries.discard('col')
print(set_countries)

# Elimina todo el conjunto
set_countries.clear()
print(set_countries)