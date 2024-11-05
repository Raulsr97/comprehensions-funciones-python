try:
    print(0 / 0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
    print(error)

print('hola')