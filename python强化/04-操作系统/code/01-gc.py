import gc
import sys
# 引用计数
# a = [1]
# print(sys.getrefcount(a))
#
# b = 1
# # 小整数对象池
# print(sys.getrefcount(b))

# 循环引用 del减少引用计数
a = [1]
b = [2]
a.append(b)
b.append(a)
print(sys.getrefcount(a))
print(sys.getrefcount(b))

# 标记清除 从根对象访问可达点, 不可达点标记清除

"""
分代回收:将创建的对象分为0 1 2代,每隔一段时间对这三代进行标记清除
"""
print(gc.get_threshold())
# (700, 10, 10)