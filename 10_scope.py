price = 100 # Esta variable tiene un alcance global dentro de este archivo

def incrementar():
    price = price + 10 # Las variables encapsuladas dentro de algun bloque de codigo solo tienen un alcance local y un contexto difererente aunque la variable se llame igual a otra que este en el contexto global
    print(price)

incrementar()
print(price)