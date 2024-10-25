numbers = []

for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

# List Comprehension [elemento, ciclo donde se extraen elementos de cualquier iterable]
numbers_v2 = [element * 2 for element in range(1,11)]
print(numbers_v2)

# List Comprehension mas condicional

numbers_v3 = [element * 2 for element in range(1, 11) if element % 2 == 0]
print(numbers_v3)


# numbers_v3 = []

# for element in range(1,11):
#     if element % 2 == 0:
#         numbers_v3.append(element * 2)

# print(numbers_v3)


