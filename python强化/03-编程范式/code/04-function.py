from functools import reduce

lst = list(map(lambda x: x * x, range(10)))
print(lst)
print(reduce(lambda x, y: x + y, range(1, 4)))

lst2 = list(filter(lambda x: x % 2 == 0, range(10)))
print(lst2)
