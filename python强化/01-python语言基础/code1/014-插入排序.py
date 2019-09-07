def insert_sort(a):
    """插入排序, 稳定, 时间复杂度n**2"""
    # 获取列表长度
    n = len(a)
    # 由于要从第二个数开始比较,所以下标应该从1开始
    for i in range(1, n):
        # 标示比较的起始位置
        j = i
        # 比较的范围
        while j > 0:
            # 如果该位置比前一位置的值大
            if a[j] < a[j-1]:
                # 交换位置
                a[j], a[j-1] = a[j-1], a[j]
                # 需要经过多次比较
                j -= 1
            else:
                # 否则不用比较,已经是一个升序列表
                break


if __name__ == '__main__':
    b = [3, 9, 1, 2, 7]
    insert_sort(b)
    print(b)
