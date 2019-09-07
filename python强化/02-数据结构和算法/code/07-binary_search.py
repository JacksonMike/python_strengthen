def binary_search(lst, value):
    # 所以时间复杂度可以表示O()=O(logn)
    n = len(lst)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False


if __name__ == '__main__':
    l = [1, 2, 4, 5, 8]
    print(binary_search(l, 0))
