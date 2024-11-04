import mod

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


def run():

    keys, values = mod.get_population()
    print(keys, values)

    country = input('Type Country => ')

    result = mod.population_by_country(data, country)
    print(result)

# Condicional que dice si el archivo es ejecutado desde la terminal ejecute el run() si es ejecutado desde otro archivo se utiliza cómo modulo
# A esto se le llama 'entry point'
if __name__ == '__main__':
    run()