def merge_sort(a):
    """归并排序,时间复杂度n*log n,稳定"""
    # 获取列表的长度
    n = len(a)
    # 将列表进行多次拆分,最终变成单个元素
    if n <= 1:
        return a
    # 拆分中界处元素下标
    middle = n // 2
    # 一值递归,使得原列表分成两个子列表
    # 采用归并排序后形成的左边有序的新序列
    left_list = merge_sort(a[:middle])
    # 采用归并排序后形成的右边有序的新序列
    right_list = merge_sort(a[middle:])
    # 将两个有序的子序列合并成一个整体,分别定义两个游标
    left_point, right_point = 0, 0
    # 定义一个空列表存储元素
    result = []
    # 当游标在子列表范围内移动
    while left_point < len(left_list) and right_point < len(right_list):
        # 如果左边的头元素小于右边的头元素
        if left_list[left_point] <= right_list[right_point]:
            # 空列表添加左边的元素
            result.append(left_list[left_point])
            # 左游标向前移动
            left_point += 1
        else:
            # 空列表添加右边的元素
            result.append(right_list[right_point])
            # 右游标向前移动
            right_point += 1
    # 添加完成后,必有一边存在剩余元素,添加至空列表末尾
    result += left_list[left_point:]
    result += right_list[right_point:]
    # 返回结果
    return result


if __name__ == '__main__':
    b = [1, 0, 2, 9, 3, 4]
    c = merge_sort(b)
    print(c)
