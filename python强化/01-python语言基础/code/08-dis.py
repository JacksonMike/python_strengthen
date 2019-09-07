import dis


def update_list(l):
    l[0] = 999


dis.dis(update_list)
"""
5           0 LOAD_CONST               1 (999)
              3 LOAD_FAST                0 (l)
              6 LOAD_CONST               2 (0)
              9 STORE_SUBSCR            # 单字节码操作线程安全
             10 LOAD_CONST               0 (None)
             13 RETURN_VALUE

Process
"""


def update_list1(l):
    l[0] += 1


dis.dis(update_list1)

"""
  5           0 LOAD_CONST               1 (999)
              3 LOAD_FAST                0 (l)
              6 LOAD_CONST               2 (0)
              9 STORE_SUBSCR
             10 LOAD_CONST               0 (None)
             13 RETURN_VALUE
 22           0 LOAD_FAST                0 (l)
              3 LOAD_CONST               1 (0)
              6 DUP_TOP_TWO
              7 BINARY_SUBSCR
              8 LOAD_CONST               2 (1)
             11 INPLACE_ADD
             12 ROT_THREE
             13 STORE_SUBSCR
             14 LOAD_CONST               0 (None)
             17 RETURN_VALUE

Process finished with exit code 0

"""