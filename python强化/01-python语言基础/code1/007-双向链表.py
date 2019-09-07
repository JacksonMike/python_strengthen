class Node(object):
    """结点"""
    def __init__(self, item):
        # 存放的元素
        self.elem = item
        # 后继结点
        self.next = None
        # 前驱结点
        self.prev = None


class DoubleLinkList(object):
    """双向链表"""
    # 头结点默认指向空
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        # 头指针指向空
        if self.__head:
            return False
        else:
            return True

    def get_length(self):
        """链表长度"""
        # 定义游标,遍历链表结点
        cur = self.__head
        # 计数器
        count = 0
        # 当游标到达末尾,即cur == None结束循环
        while cur:
            # 只要开启循环,计数器加一
            count += 1
            # 游标向后移动
            cur = cur.next
        # 计数器数字即为结点数
        return count

    def travel_list(self):
        """遍历链表"""
        # 定义游标遍历结点
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
        # 如果为空链表,头结点直接指向新结点
        if self.is_empty():
            self.__head = node
        else:
            # 创建游标并使其到达尾结点
            cur = self.__head
            # 游标移动的范围
            while cur.next:
                # 移动游标
                cur = cur.next
            # node前驱指向cur
            node.prev = cur
            # cur的后继指向node
            cur.next = node

    def add_elem(self, item):
        """链表头部添加元素,头插法"""
        # 建立新的结点
        node = Node(item)
        # 如果为空链表,头结点直接指向新结点
        if self.is_empty():
            self.__head = node
        else:
            # 将node的后继指向头指针指向区域
            node.next = self.__head
            # 头指针指向node结点
            self.__head = node
            # node结点的后继结点前驱指向node自身
            node.next.prev = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        # pos从0开始添加,如果小于等于0,则默认为头插法.如果大于length()-1,则视为尾插法
        if pos <= 0:
            self.add_elem(item)
        elif pos > self.get_length() - 1:
            self.append_elem(item)
        else:
            # 定义游标,由于要改变pos前一结点的指向,游标最终停留在pos的前驱结点
            cur = self.__head
            # 计数器
            count = 0
            # 循环结束后游标位于pos前趋结点
            while count < pos - 1:
                count += 1
                # 移动游标
                cur = cur.next
            # 创造结点
            node = Node(item)
            # node的next域指向cur的next域名
            node.next = cur.next
            # cur的next域指向node
            cur.next = node
            # node的prev指向cur的后继结点的prev域名
            node.prev = cur.next.prev
            # cur的后继结点的prev指向node
            cur.next.prev = node

    def find(self, item):
        """查找结点是否存在"""
        # 定义游标遍历结点
        cur = self.__head
        # 计数器,记录结点下表
        count = 0
        # 游标移动范围
        while cur:
            # 进入循环后,count+1
            count += 1
            # 如果遍历结点的数据域和查找值相等返回True
            if cur.elem == item:
                print("所找结点下标:%d" % (count - 1))
                return True
            # 否则继续移动游标
            else:
                cur = cur.next
        # 当遍历完链表时候,仍然没发现所给值,即所找结点不存在
        print("结点不存在")
        return False

    def remove(self, item):
        """删除链表任意结点"""
        # 创建游标指向头结点
        cur = self.__head
        # 游标移动范围
        while cur:
            # 判断结点是否匹配元素
            if cur.elem == item:
                # 如果要删除头结点
                if cur == self.__head:
                    # 如果链表多于一个结点(两个及以上)
                    if cur.next:
                        # 头指针指向cur的next域名
                        self.__head = cur.next
                        # cur的next域名的prev域指向空
                        cur.next.prev = None
                    # 仅仅一个结点
                    else:
                        # 头指针指向cur的next域名
                        self.__head = cur.next
                else:
                    # 如果删除不是尾结点
                    if cur.next:
                        # cur前驱结点的next指向cur的next
                        cur.prev.next = cur.next
                        # cur后继结点的prev指向cur的prev
                        cur.next.prev = cur.prev
                    # 删除尾结点
                    else:
                        # cur前驱结点的next指向cur的next
                        cur.prev.next = cur.next
                # 删除结点后立即结束整个循环
                break
            else:
                # 继续移动游标
                cur = cur.next


if __name__ == '__main__':
    # 创建链表对象
    dll = DoubleLinkList()
