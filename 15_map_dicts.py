items = [
    {
        'producto': 'camisa',
        'precio': 100
    },
    {
        'producto': 'pantalon',
        'precio': 200
    },
    {
        'producto': 'tenis',
        'precio': 1000
    }
]

precios = list(map(lambda items : items['precio'], items))
print(f'Precios: {precios}')

productos = list(map(lambda items : items['producto'], items))
print(f'Productos: {productos}')

print(items)

# Agregando atributo nuevo al diccionario:
def agregar_impuestos(item):
    item['impuestos'] = item['precio'] * .10
    return item
 
new_items = list(map(agregar_impuestos, items))
print(new_items)