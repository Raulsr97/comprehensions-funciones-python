import random

# dict = {}
# for i in range(1, 11):
#     dict[i] = i * 2

# print(dict)

# Dictonary comprehension

dict_2 = {i: i * 2 for i in range(1, 5)}
print(dict_2)

dict_3 = {i: i + 2 for i in range(1, 6)}
print(dict_3)


# Generando diccionario a partir de una lista
countries = ['col', 'mex', 'bol', 'bra']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)

print(population)

# version comprimida:
population_v2 = {country : random.randint(1, 100) for country in countries}
print(population_v2)


# Generando un diccionario a partir de dos listas
names = ['Raul', 'Cristiano', 'Messi']
ages = [26, 38, 36]

players = {name: age for (name, age) in zip(names, ages)}
print(players)


