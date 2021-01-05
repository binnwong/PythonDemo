# coding=utf-8
class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None


class TreeQueue(object):
    def __init__(self):
        self.__members = list()

    def is_empty(self):
        return not len(self.__members)

    def enter(self, data):
        self.__members.insert(0, data)

    def outer(self):
        if self.is_empty():
            return
        return self.__members.pop()


class PerfectBinaryTree(object):

    def __init__(self):
        self.__root = None

    def is_empty(self):
        return not self.__root

    def append(self, data):
        node = Node(data)
        if self.is_empty():
            self.__root = node
            return
        queue = TreeQueue()
        queue.enter(self.__root)
        while not queue.is_empty():
            cur = queue.outer()
            if cur.left_child is None:
                cur.left_child = node
                node.parent = cur
                return
            queue.enter(cur.left_child)
            if cur.right_child is None:
                cur.right_child = node
                node.parent = cur
                return
            queue.enter(cur.right_child)

    def show(self):
        if self.is_empty():
            print('空二叉树')
            return
        queue = TreeQueue()
        queue.enter(self.__root)
        while not queue.is_empty():
            cur = queue.outer()
            print(cur.data, end=' ')
            if cur.left_child is not None:
                queue.enter(cur.left_child)
            if cur.right_child is not None:
                queue.enter(cur.right_child)
        print()

    def get_root(self):
        return self.__root


# 先根遍历（先序遍历）
def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder_traversal(root.left_child)
    preorder_traversal(root.right_child)


# 中根遍历（中序遍历）
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left_child)
    print(root.data, end=' ')
    inorder_traversal(root.right_child)


# 后根遍历（后序遍历）
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left_child)
    postorder_traversal(root.right_child)
    print(root.data, end=' ')


if __name__ == '__main__':
    tree = PerfectBinaryTree()
    for alpha in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
        tree.append(alpha)
    print('层次遍历： ', end='')
    tree.show()
    print('先序遍历： ', end='')
    preorder_traversal(tree.get_root())
    print()
    print('中序遍历： ', end='')
    inorder_traversal(tree.get_root())
    print()
    print('后序遍历： ', end='')
    postorder_traversal(tree.get_root())
    print()
