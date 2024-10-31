# def incremement(x):
#     return x + 1

increment = lambda x : x + 1

# def high_ord_func(x, func):
#     return x + func(x)

high_ord_func = lambda x, func : x + func(x)

result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)

