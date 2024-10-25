set_a = {'mex', 'col', 'bra'}
set_b = {'mex', 'pan', 'par'}

# Union de conjuntos
set_c = set_a.union(set_b)
print(set_c)

print(set_a | set_b)

# Interseccion de conjuntos

set_c = set_a.intersection(set_b)
print(set_c)

print(set_a & set_b)

# Realiza la operacion diferencia entre dos conjuntos
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

# Realiza la diferencia simetrica entre dos conjuntos, es decir solo se eliminaran loa elementos en común
set_c = set_a.symmetric_difference(set_b)
print(set_c)

print(set_a ^ set_b)