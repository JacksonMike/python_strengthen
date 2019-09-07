from timeit import Timer


# 对创建列表的不同方式进行时间测算
def t1():
    """append生成列表"""
    a = []
    for i in range(1000):
        a.append(i)


def t2():
    """列表相加"""
    a = []
    for i in range(1000):
        # 生产一个新的列表,将两个原来的列表中的元素添加至新列表
        a = a + [i]


def t3():
    """列表生成器"""
    a = [i for i in range(1000)]


def t4():
    """将可以迭代的对象强转成为列表"""
    # 效率最高
    a = list(range(1000))


def t5():
    a = []
    # 效率最低
    for i in range(1000):
        # 将列表加到a,没有产生新列表
        a.extend([i])


# 添加元素方式
def t6():
    # 效率更高
    b = []
    for i in range(1000):
        b.append(i)


def t7():
    b = []
    for i in range(1000):
        b.insert(0, i)


s1 = Timer("t1()", "from __main__ import t1")
print(s1.timeit(number=10000))
s2 = Timer("t2()", "from __main__ import t2")
print(s2.timeit(number=10000))
s3 = Timer("t3()", "from __main__ import t3")
print(s3.timeit(number=10000))
s4 = Timer("t4()", "from __main__ import t4")
print(s4.timeit(number=10000))
s5 = Timer("t5()", "from __main__ import t5")
print(s5.timeit(number=10000))
s6 = Timer("t6()", "from __main__ import t6")
print(s6.timeit(number=10000))
s7 = Timer("t7()", "from __main__ import t7")
print(s7.timeit(number=10000))





