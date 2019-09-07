def quick_sort(a, first, last):
    """快速排序,时间复杂度n**2,每次分仅有一个元素,不稳定"""
    # 递归结束条件,列表只有一个元素,
    # 递归函数中没有return返回的对象,默认返回return的一个None对象
    if first >= last:
        return
    # 设置中间值,默认为第一个元素
    middle_value = a[first]
    # 分别设置两个游标进行分区,first和last为操作的区间
    low = first
    high = last
    # 分区结束标志
    while low < high:
        # 首先将游标high向左移动,循环移动
        while low < high and a[high] >= middle_value:
            high -= 1
        # 否则low指向high的域,high置为空
        a[low] = a[high]
        # 再将游标low向右移动
        while low < high and a[low] < middle_value:
            low += 1
        # 否则high指向low域,low置为空
        a[high] = a[low]
    # 当循环结束的时,low == high
    a[low] = middle_value
    # 此时以middle_value为界,列表分成两个子列表
    # 对low左边的子列表进行递归
    quick_sort(a, first, low - 1)
    # 对low右边的子列表进行递归
    quick_sort(a, low + 1, last)


if __name__ == '__main__':
    b = [2, 7, 9, 4, 3]
    print(b)
    quick_sort(b, 0, len(b) - 1)
    print(b)
    print(quick_sort(b, 0, len(b) - 1))




