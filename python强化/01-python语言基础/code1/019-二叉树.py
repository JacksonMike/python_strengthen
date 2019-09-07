class Node(object):
    """结点"""
    def __init__(self, item):
        # 数据域
        self.elem = item
        # 左子数
        self.left_child = None
        # 右子数
        self.right_child = None


class Tree(object):
    """二叉树"""
    def __init__(self):
        # 根结点指向空
        self.root = None

    def add(self, item):
        # 创建新结点
        node = Node(item)
        # 首先让根结点指向新结点
        if self.root is None:
            self.root = node
            return
        # 创建队列来存储结点,队列先进先出
        queue = [self.root]
        # 当队列不为空的时候
        while queue:
            # 获取当前要操作的结点
            current_node = queue.pop(0)
            # 如果当前结点的左结点为空
            if current_node.left_child is None:
                # 左结点指向新结点
                current_node.left_child = node
                return
            else:
                # 添加到队列中
                queue.append(current_node.left_child)
            # 如果当前结点的右结点为空
            if current_node.right_child is None:
                # 右结点指向新结点
                current_node.right_child = node
                return
            else:
                # 添加到队列中
                queue.append(current_node.right_child)

    def breadth_travel(self):
        # 如果根结点为空,不用遍历,递归终止条件
        if self.root is None:
            return
        # 将结点存储在队列中
        queue = [self.root]
        # 当队列不为空时
        while queue:
            # 获取当前要操作的结点
            current_node = queue.pop(0)
            # 打印结点对应的数据
            print(current_node.elem, end=" ")
            # 如果左子树非空,将左子树结点添加到对列中
            if current_node.left_child:
                queue.append(current_node.left_child)
            # 如果右子树非空,将右子树结点添加到对列中
            if current_node.right_child:
                queue.append(current_node.right_child)

    def pre_order(self, node):
        # 如果结点为空,不用遍历,递归终止条件
        if node is None:
            return
        # 打印根结点的元素
        print(node.elem, end=" ")
        # 遍历左子树
        self.pre_order(node.left_child)
        # 遍历右子树
        self.pre_order(node.right_child)

    def in_order(self, node):
        # 如果结点为空,不用遍历,递归终止条件
        if node is None:
            return
        # 遍历左子树
        self.in_order(node.left_child)
        # 打印根结点的元素
        print(node.elem, end=" ")
        # 遍历右子树
        self.in_order(node.right_child)

    def post_order(self, node):
        # 如果结点为空,不用遍历,递归终止条件
        if node is None:
            return
        # 遍历左子树
        self.post_order(node.left_child)
        # 遍历右子树
        self.post_order(node.right_child)
        # 打印根结点的元素
        print(node.elem, end=" ")


if __name__ == '__main__':
    # 创建对象
    tree = Tree()
    # 添加元素
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.post_order(tree.root)
    print("")
    tree.in_order(tree.root)


