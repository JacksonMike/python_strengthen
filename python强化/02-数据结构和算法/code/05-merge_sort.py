def merge_sort(lst):
    a = len(lst)
    if a <= 1:
        return lst
    middle = a // 2
    left_part = merge_sort(lst[:middle])
    right_part = merge_sort(lst[middle:])
    left_point, right_point = 0, 0
    result = []
    while left_point < len(left_part) and right_point < len(right_part):
        if left_part[left_point] <= right_part[right_point]:
            result.append(left_part[left_point])
            left_point += 1
        else:
            result.append(right_part[right_point])
            right_point += 1
    result += left_part[left_point:]
    result += right_part[right_point:]
    return result


if __name__ == '__main__':
    l = [1, 3, 2, 5, 8, 4]
    print(merge_sort(l))
