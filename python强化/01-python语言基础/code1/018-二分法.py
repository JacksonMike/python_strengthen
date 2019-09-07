def binary_search(sequence_list, item):
    """二分法 要传入有顺序的顺序表"""
    # 获取列表长度
    n = len(sequence_list)
    # 定义两个游标
    first = 0
    last = n - 1
    # 两个游标之间的关系
    while first <= last:
        # 获取中间值
        middle = (first + last) // 2
        # 假设所找元素恰好是中间值
        if sequence_list[middle] == item:
            return True
        # 中间值大于所找元素
        elif sequence_list[middle] > item:
            # 移动last游标
            last = middle - 1
        else:
            # 移动first游标
            first = middle + 1
    # 当循环结束仍然没找到则
    return False


def binary_research_2(sequence_list, item):
    """二分法递归"""
    # 获取列表长度
    n = len(sequence_list)
    if n > 0:
        # 每次取中间位置
        middle = n // 2
        # 如果所找元素与中间位置对应元素相等
        if sequence_list[middle] == item:
            return True
        # 如果大于中间值
        elif sequence_list[middle] > item:
            # 递归,操作区间为开头至中间值
            return binary_research_2(sequence_list[:middle], item)
        # 如果小于中间值
        else:
            # 递归,操作区间为中间值至结尾
            return binary_research_2(sequence_list[middle + 1:], item)
    # 还没找到即没有该元素
    return False


if __name__ == '__main__':
    a = [1, 3, 6, 8, 9, 16]
    print(binary_search(a, 111))
    print(binary_research_2(a, 90))
