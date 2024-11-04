def get_population():
    keys = ['Mex', 'Arg', 'Col']
    values = [1000, 700, 500]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result