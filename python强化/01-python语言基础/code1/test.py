def sort(a, b):
    if a % b == 0:
        return b
    else:
        sort(a, a % b)


print(sort(4, 2))

