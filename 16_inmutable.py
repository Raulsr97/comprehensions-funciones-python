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

def agregar_impuestos(item):
    new_item = item.copy()
    new_item['impuestos'] = new_item['precio'] * .10
    return new_item
 
new_items = list(map(agregar_impuestos, items))
print('New List')
print(new_items)
print('Old list')
print(items)

