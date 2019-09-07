def quick_sort(lst, first, last):
    if first >= last:
        return None
    middle_value = lst[first]
    low = first
    high = last
    # low指向比mid小的值,high指向比mid大的值,出现异常的话就要交换
    while low < high:
        while low < high and lst[high] >= middle_value:
            high -= 1
        lst[low] = lst[high]
        while low < high and lst[low] < middle_value:
            low += 1
        lst[high] = lst[low]
    lst[low] = middle_value
    quick_sort(lst, first, low - 1)
    quick_sort(lst, low + 1, last)
    return lst


if __name__ == '__main__':
    l = [1, 4, 2, 5, 3]
    print(quick_sort(l, 0, len(l) - 1))
