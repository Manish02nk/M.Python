from functools import reduce
l = [3, 8, 4, 2, 5, 45, 47]

a = reduce(max, l)
print(a)
