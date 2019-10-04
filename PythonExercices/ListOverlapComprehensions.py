#List Overlap Comprehensions


import random

a = random.sample(range(100), 5)
b = random.sample(range(100), 10)
result = [i for i in a if i in b]
print (result)