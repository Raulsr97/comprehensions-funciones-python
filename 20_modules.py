import sys
print(sys.path)

import re

text = 'Mi numero es 5611861455, el numero de mi casa es 272'

result = re.findall('[0-9]+', text)
print(result)

import time

timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)

import collections

numbers = [1, 2, 3, 3, 3, 1, 1 , 4, 4, 5]
counter = collections.Counter(numbers)
print(counter)