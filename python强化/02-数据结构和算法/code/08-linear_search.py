def linear_search(lst, value):
    # 时间复杂度：O(n)
    for i in range(len(lst) - 1):
        if lst[i] == value:
            return True
    return False


if __name__ == '__main__':
    l = [1, 2, 8, 3]
    print(linear_search(l, 2))
