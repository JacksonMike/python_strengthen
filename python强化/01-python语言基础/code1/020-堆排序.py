from heapq import heappush, heappop


def heap_sort(lst):
    temp = []
    # 入堆
    for item in lst:
        heappush(temp, item)
    # 清空列表
    lst.clear()
    # 出堆
    for i in range(len(temp)):
        lst.append(heappop(temp))


l = [1, 2, 3, 4, 0, 9, 2, 3]
heap_sort(l)
print(l)
