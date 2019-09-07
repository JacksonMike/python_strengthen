class Node(object):
    """结点"""
    def __init__(self, item):
        # 存放的元素
        self.elem = item
        # 下一结点的标识
        self.next = None


class LinkList(object):
    """单链表"""
    # 头指针默认指向空
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        # 头指针是否指向空
        if self.__head:
            return False
        else:
            return True

    def get_length(self):
        """链表长度"""
        # 游标用来遍历结点
        cur = self.__head
        # 计数器
        count = 0
        # 当游标到达末尾,即cur == None结束循环
        while cur:
            # 只要开启循环,计数器加一
            count += 1
            # 游标向后移动
            cur = cur.next
        # count数即为结点数
        return count

    def travel_list(self):
        """遍历链表"""
        # 游标用来遍历结点
        cur = self.__head
        # 计数器
        count = 0
        # 当游标到达末尾,即cur == None结束循环
        while cur:
            # 只要开启循环,计数器加一
            count += 1
            # 打印存储的值
            print(cur.elem, end=" ")
            # 游标向后移动
            cur = cur.next

    def append_elem(self, item):
        """链表尾部添加元素,尾插法"""
        # 建立新结点
        node = Node(item)
        # 如果空链表直接指向新结点
        if self.is_empty():
            self.__head = node
        else:
            # 设置游标指向头指针域
            cur = self.__head
            # 判断是否到达当前的尾结点
            while cur.next:
                # 移动游标
                cur = cur.next
            # cur的next域指向node
            cur.next = node

    def add_elem(self, item):
        """链表头部添加元素,头插法"""
        # 建立新的结点
        node = Node(item)
        # 如果空链表直接指向新结点
        if self.is_empty():
            self.__head = node
        # node的next域指向头指针
        node.next = self.__head
        # 头指针指向node
        self.__head = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        # pos从0开始添加,如果小于等于0,则默认为头插法.如果大于length()-1,则视为尾插法
        if pos <= 0:
            self.add_elem(item)
        elif pos > self.get_length() - 1:
            self.append_elem(item)
        else:
            # 定义游标,由于要改变pos前一结点的指向,游标最终停留在pos的前驱结点
            pre = self.__head
            # 计数器
            count = 0
            # 循环结束后游标位于pos前一结点
            while count < pos - 1:
                count += 1
                # 移动游标
                pre = pre.next
            # 创造新结点
            node = Node(item)
            # node的next域指向pre的next域
            node.next = pre.next
            # pre的next域指向node
            pre.next = node

    def find(self, item):
        """查找结点是否存在"""
        # 定义游标对链表进行遍历
        cur = self.__head
        # 定义计数器记录所找结点的下标
        count = 0
        # 游标移动范围
        while cur:
            # 进入循环后,count+1
            count += 1
            # 如果遍历结点的数据域和查找值相等返回True
            if cur.elem == item:
                # 打印结点下标
                print("结点下标为:%d" % count)
                return True
            # 否则继续移动游标
            else:
                cur = cur.next
        # 当遍历完链表时候,仍然没发现所给值,即所找结点不存在
        print("结点不存在")
        return False

    def remove(self, item):
        """删除链表任意结点"""
        # 创建两个游标,她们最终指向要删除的结点和他的前驱结点
        cur = self.__head
        pre = None
        # 游标移动范围
        while cur:
            # 如果遍历的数据域与要删除数据域相等,则进行删除
            if cur.elem == item:
                # 如果要删除头结点
                if cur == self.__head:
                    # 将头结点的next域指向cur的next域
                    self.__head = cur.next
                else:
                    # 否则将pre的next域指向cur的next域
                    pre.next = cur.next
                break
            else:
                # 否则同时移动两个游标
                pre = cur
                cur = cur.next


if __name__ == '__main__':
    ll = LinkList()
    ll.append_elem(3)
    ll.append_elem(4)
    ll.append_elem(5)
    ll.append_elem(7)
    print(ll.find(8))
    ll.travel_list()



