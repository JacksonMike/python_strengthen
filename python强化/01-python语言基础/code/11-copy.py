import copy

lst1 = [1, 2, [4, 5]]
lst2 = copy.copy(lst1)
lst1[2].append(6)
print(lst1, lst2)

lst3 = [1, 2, [6, 7]]
lst4 = copy.deepcopy(lst3)
lst3[2].append(8)
print(lst3, lst4)
