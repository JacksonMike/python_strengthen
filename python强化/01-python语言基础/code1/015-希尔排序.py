def shell_sort(a):
    """希尔排序:按照步长选择出子列表 进行插入排序 直到步长为1"""
    # 获取列表长度
    n = len(a)
    # 获取步长值
    gap = n // 2
    while gap > 0:
        # 当成插入算法,但此时i从下标为gap的位置开始比较,一个for循环控制多个子列表
        for i in range(gap, n):
            # 用比较的轮数来结合比较的起始位置
            j = i
            # 确立要比较的范围
            while j > 0:
                # 如果该项大于前一项
                if a[j] < a[j - gap]:
                    # 交换位置
                    a[j], a[j - gap] = a[j - gap], a[j]
                    # 需要多次比较,j要移动
                    j -= gap
                else:
                    # 否则,直接跳出循环
                    break
        # 缩短步长
        gap = gap // 2


if __name__ == '__main__':
    b = [8, 7, 3, 4, 2, 1]
    shell_sort(b)
    print(b)



