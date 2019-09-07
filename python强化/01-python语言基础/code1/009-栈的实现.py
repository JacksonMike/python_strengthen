# 利用顺序表,即python中的列表来实现栈
class Stack(object):
    """栈"""
    def __init__(self):
        # 初始值设置为一个链表
        self.__list = []

    def push(self, item):
        """入栈"""
        # 添加元素至栈顶
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        # 如果为非空链表
        if self.__list:
            return self.__list[-1]
        # 如果为空链表
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        # 先判断return右边的式子,返回该式子的返回值
        return self.__list == []

    def get_size(self):
        """获取栈中元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    # 创建对象
    s = Stack()
