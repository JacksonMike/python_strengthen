from heapq import *


def heap_sort(lst):
    result = []
    # 入堆
    for value in lst:
        heappush(result, value)
    # 出堆
    # result2 = []
    # for i in range(len(result)):
    #     result2.append(heappop(result))
    # return result2
    return [heappop(result) for i in range(len(result))]


print(heap_sort([1, 2, 3, 8, 4]))
