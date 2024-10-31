def increment(x):
    return x + 1

result = increment(10)
print(result)

# lambda, parametro de entrada, parametro de salida, se puede asignar el valor a una variable
incremement_v2 = lambda x : x + 1
result_v2 = incremement_v2(5)
print(result_v2)


full_name = lambda name, last_name : f'full name is {name.title()} {last_name.title()}'

text = full_name('raul', 'salinas')
print(text)