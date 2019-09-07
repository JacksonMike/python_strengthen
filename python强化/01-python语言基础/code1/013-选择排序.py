def select_sort(a):
    """选择排序,不稳定, 时间复杂度n**2"""
    # 获取列表的长度
    n = len(a)
    # 确定比较的趟数
    for i in range(n - 1):
        # 默认最小项的下标
        c = i
        # 确立要比较的范围
        for j in range(i + 1, n):
            # 如果小于最小项
            if a[j] < a[i]:
                c = j
                # 交换位置
                a[i], a[c] = a[c], a[i]


b = [11, 2, 3, 9, 83, 1, 33, 24, 5]
select_sort(b)
print(b)
