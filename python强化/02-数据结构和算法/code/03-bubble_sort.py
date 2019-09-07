def bubble_sort(lst):
    a = len(lst)
    for i in range(a - 1):
        for j in range(a - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == '__main__':
    l = [1, 5, 3, 2, 9]
    print(bubble_sort(l))
