# 元素可以在任意一端出队和如队
class DoubleDeque(object):
    """双端队列"""
    def __init__(self):
        # 仍然用列表来存储双端对列
        self.__list = []

    def add_front(self, item):
        """在队列头部添加元素"""
        return self.__list.insert(0, item)

    def pop_front(self):
        """在队列头部删除元素"""
        return self.__list.pop(0)

    def add_rear(self, item):
        """在对列尾部添加元素"""
        return self.__list.append(item)

    def pop_rear(self):
        """在队列尾部删除元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断是否为空"""
        return self.__list == []

    def get_length(self):
        """获取对列中对元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    dq = DoubleDeque()
