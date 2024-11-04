import mod

keys, values = mod.get_population()
print(keys, values)

data = [
    {
        'Country': 'Colombia',
        'Population': 300
    },
    {
        'Country': 'Mexico',
        'Population': 1000
    },
]

country = input('Type Country => ')

result = mod.population_by_country(data, country)
print(result)