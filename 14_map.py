numbers = [1, 2, 3, 4, 5]
numbers_v2 = []

for number in numbers:
    numbers_v2.append(number * 2)

print(numbers)
print(numbers_v2)

# Utilizando map() y lambda functions para resolver el ejercicio anterior

numbers_v3 = list(map(lambda number : number * 3, numbers)) 
print(numbers_v3)


numbers_1 = [1, 2, 3]
numbers_2 = [4, 5, 6]

numbers_3 = list(map(lambda x, y : x + y, numbers_1, numbers_2))

print(numbers_1)
print(numbers_2)
print(numbers_3)
 