class Node(object):
    """结点"""
    def __init__(self, item):
        # 存放的元素
        self.elem = item
        # 下一结点的标识
        self.next = None


class CycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        # 将结点初始值设置为空,如果没传入结点,即为空链表,头结点默认指向空
        self.__head = node
        # 如果传入的为非空结点,node的next域指向本身
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        # 头结点指向空
        if self.__head:
            return False
        else:
            return True

    def get_length(self):
        """链表长度"""
        # 如果为空链表,长度为0
        if self.is_empty():
            return 0
        # 定义游标来遍历结点
        cur = self.__head
        # 定义计数器
        count = 1
        # 游标到达尾结点的条件为该结点的next域指向头指针域
        while cur.next != self.__head:
            # 计数器记录移动数量
            count += 1
            # 游标移动
            cur = cur.next
        # 返回值即为链表长度
        return count

    def travel_list(self):
        """遍历链表"""
        # 如果链表为空,不能遍历
        if self.is_empty():
            return False
        # 定义游标来遍历结点
        cur = self.__head
        # 游标到达尾结点条件
        while cur.next != self.__head:
            # 打印游标数据域
            print(cur.elem, end=" ")
            # 将游标向后移动
            cur = cur.next
        # 由于游标到达尾结点时已经退出了,还需要打印最后一个结点的数据域
        print(cur.elem)

    def append_elem(self, item):
        """链表尾部添加元素,尾插法"""
        # 建立新结点
        node = Node(item)
        # 如果空链表直接指向新结点,新结点next域直接指向本身
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 设置游标指向头指针
            cur = self.__head
            # 判断游标是否到达当前的尾结点
            while cur.next != self.__head:
                # 移动游标
                cur = cur.next
            # node的next域指向cur的next域
            node.next = cur.next
            # cur的next域指向node
            cur.next = node

    def add_elem(self, item):
        """链表头部添加元素,头插法"""
        # 建立新的结点
        node = Node(item)
        # 如果为空链表,新结点next域直接指向本身
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            # 先使游标移动到尾结点
            while cur.next != self.__head:
                # 移动游标
                cur = cur.next
            # node的next域指向头指针域
            node.next = self.__head
            # 头指针域指向node
            self.__head = node
            # cur的next域指向node
            cur.next = node

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
        # 如果为空链表,则返回False
        if self.is_empty():
            return False
        # 定义计数器,记录结点下标
        count = 0
        # 定义游标遍历结点
        cur = self.__head
        # 将游标移动到尾结点
        while cur.next != self.__head:
            # 进入循环,计数器+1
            count += 1
            # 如果游标数据域等于所查找元素
            if cur.elem == item:
                # 打印下标
                print("结点下标:%d" % (count - 1))
                return True
            else:
                # 继续移动游标
                cur = cur.next
        # 此时游标位于尾结点,再次判断游标数据域是否与查找元素相等
        if cur.elem == item:
            # 打印结点下标
            print("结点下标:%d" % count)
            return True
        # 当所有结点都判断完成后仍然没有
        print("结点不存在")
        return False

    def remove(self, item):
        """删除链表任意结点"""
        # 如果为空链表不需要删除
        if self.is_empty():
            return False
        # 定义两个游标,分别最终指向要删除的结点和其前驱结点
        cur = self.__head
        pre = None
        # 将cur游标移动到尾结点
        while cur.next != self.__head:
            # 数据域与元素相匹配
            if cur.elem == item:
                # 如果要删除的结点是头结点
                if cur == self.__head:
                    # 定义游标寻找尾结点
                    rear = self.__head
                    # 通过循环移动
                    while rear.next != self.__head:
                        # 移动游标
                        rear = rear.next
                    # 头指针域指向cur的next域
                    self.__head = cur.next
                    # rear结点的next域指向头指针域
                    rear.next = self.__head
                else:
                    # 如果删除中间结点
                    """由于删除的不是头结点时候,已经将pre指向了cur,形成了两个游标"""
                    # pre的next域指向cur的next域
                    pre.next = cur.next
                # 结束部分while循环,如果用break则整个结束了
                return
            else:
                # pre指向原来cur指向处
                pre = cur
                # cur向后移动
                cur = cur.next
        # 通过循环后cur已经指向尾结点了,如果尾结点的数据域与元素相匹配
        if cur.elem == item:
            # 如果链表只有一个结点,即
            if cur == self.__head:
                # 头指针域指向空
                self.__head = None
            else:
                # 前驱结点的next域指向头指针域
                pre.next = self.__head


if __name__ == '__main__':
    cll = CycleLinkList()
    cll.append_elem(1)
    cll.append_elem(2)
    cll.remove(2)
    cll.travel_list()


