def bubble_sort(a):
    """冒泡排序, 不稳定, 时间复杂度n**2"""
    # 获取列表长度
    n = len(a)
    # 控制比较趟数
    for i in range(n-1):
        # 记录每一天交换次数
        count = 0
        # 控制每一趟比较次数
        for j in range(n-1-i):
            # 如果前一项大于后一项交换位置
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
        # 如果这一趟没有出现交换,则表明这一趟是已经有序
        if 0 == count:
            # 直接退出循环
            break


if __name__ == '__main__':
    b = [33, 88, 11, 2, 9]
    bubble_sort(b)
    print(b)
