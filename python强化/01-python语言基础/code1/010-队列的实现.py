class Queue(object):
    """对列"""
    # 用列表实现队列
    def __init__(self):
        # 队列以列表的形式存储
        self.__list = []

    def enqueue(self, item):
        """入队"""
        self.__list.append(item)

    def dequeue(self):
        """出队"""
        if self.is_empty():
            return None
        else:
            return self.__list.pop(0)

    def is_empty(self):
        """判断是否为空"""
        return self.__list == []

    def get_length(self):
        """获取对列中对元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    