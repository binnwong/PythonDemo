# coding=utf-8
class Node(object):
    """节点类"""
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.parent = None
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree(object):
    """二叉树类"""
    def __init__(self):
        self.__root = None
        self.prefix_branch = '├'
        self.prefix_trunk = '|'
        self.prefix_leaf = '└'
        self.prefix_empty = ''
        self.prefix_left = '─L─'
        self.prefix_right = '─R─'

    def is_empty(self):
        return not self.__root

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, data):
        self.__root = Node(data)

    def show_tree(self):
        if self.is_empty():
            print('空二叉树')
            return
        print('-' * 20)
        print(self.__root.data)
        self.__print_tree(self.__root)
        print('-' * 20)

    def add_left_child(self, parent, value):
        """添加左子节点"""
        if parent is None:
            print("父节点不存在")
            return
        if parent.left_child is not None:
            print("父节点已有左子节点")
            return
        node = value if isinstance(value, Node) else Node(value)
        parent.left_child = node
        node.parent = parent

    def add_right_child(self, parent, value):
        """添加右子节点"""
        if parent is None:
            print("父节点不存在")
            return
        if parent.right_child is not None:
            print("父节点已有右子节点")
            return
        node = value if isinstance(value, Node) else Node(value)
        parent.right_child = node
        node.parent = parent

    def levelorder_traversal(self):
        """层序遍历"""
        if self.is_empty():
            print('空二叉树')
            return
        queue = list()
        queue.insert(0, self.__root)
        while len(queue):
            cur = queue.pop()
            print(cur.data, end=' ')
            if cur.left_child is not None:
                queue.insert(0, cur.left_child)
            if cur.right_child is not None:
                queue.insert(0, cur.right_child)
        print()

    def preorder_traversal(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.data, end=' ')
        self.preorder_traversal(node.left_child)
        self.preorder_traversal(node.right_child)

    def inorder_traversal(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder_traversal(node.left_child)
        print(node.data, end=' ')
        self.inorder_traversal(node.right_child)

    def postorder_traversal(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder_traversal(node.left_child)
        self.postorder_traversal(node.right_child)
        print(node.data, end=' ')

    def height(self, root):
        """二叉树的深度"""
        if root.data is None:
            return 0
        if root.left_child is None and root.right_child is None:
            return 1
        if root.left_child is not None and root.right_child is None:
            return 1 + self.height(root.left_child)
        if root.left_child is None and root.right_child is not None:
            return 1 + self.height(root.right_child)
        if root.left_child is not None and root.right_child is not None:
            return 1 + max(self.height(root.left_child), self.height(root.right_child))

    def leaves(self, root):
        """二叉树的叶节点"""
        if root.data is None:
            return None
        if root.left_child is None and root.right_child is None:
            print(root.data, end=' ')
        if root.left_child is not None:
            self.leaves(root.left_child)
        if root.right_child is not None:
            self.leaves(root.right_child)

    def node_count(self, root):
        """二叉树的节点个数"""
        return self.node_count(root.left_child) + self.node_count(root.right_child) + 1 if root else 0

    def kth_node_count(self, root, k):
        """二叉树第k层的节点个数"""
        if not root or k <= 0:
            return 0
        if k == 1:
            return 1
        return self.kth_node_count(root.left_child, k-1) + self.kth_node_count(root.right_child, k-1)

    def __print_tree(self, node, prefix=None):
        if prefix is None:
            prefix, prefix_left_child = '', ''
        else:
            prefix = prefix.replace(self.prefix_branch, self.prefix_trunk)
            prefix = prefix.replace(self.prefix_leaf, self.prefix_empty)
            prefix_left_child = prefix.replace(self.prefix_leaf, self.prefix_empty)
        if self.has_child(node):
            if node.right_child is not None:
                print(prefix + self.prefix_branch + self.prefix_right + str(node.right_child.data))
                if self.has_child(node.right_child):
                    self.__print_tree(node.right_child, prefix + self.prefix_branch + ' ')
            else:
                print(prefix + self.prefix_branch + self.prefix_right)
            if node.left_child is not None:
                print(prefix + self.prefix_leaf + self.prefix_left + str(node.left_child.data))
                if self.has_child(node.left_child):
                    prefix_left_child += '  '
                    self.__print_tree(node.left_child, self.prefix_leaf + prefix_left_child)
            else:
                print(prefix + self.prefix_leaf + self.prefix_left)

    def has_child(self, node):
        return node.left_child is not None or node.right_child is not None

    def __str__(self):
        return str(self.__class__)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = 'A'
    node1 = Node('B')
    tree.add_left_child(tree.root, node1)
    node2 = Node('C')
    tree.add_right_child(tree.root, node2)
    node3 = Node('D')
    node4 = Node('E')
    node5 = Node('F')
    tree.add_right_child(node1, node3)
    tree.add_left_child(node2, node4)
    tree.add_right_child(node2, node5)
    tree.add_left_child(node3, 'G')
    tree.add_left_child(node4, 'H')
    tree.add_right_child(node4, 'I')
    tree.add_right_child(node5, 'J')
    tree.show_tree()

    print('层次遍历： ', end='')
    tree.levelorder_traversal()
    print('先序遍历： ', end='')
    tree.preorder_traversal(tree.root)
    print()
    print('中序遍历： ', end='')
    tree.inorder_traversal(tree.root)
    print()
    print('后序遍历： ', end='')
    tree.postorder_traversal(tree.root)
    print()

    print('二叉树的深度为：', tree.height(tree.root))
    print('二叉树的叶节点有：', end='')
    tree.leaves(tree.root)
    print()
    print('二叉树的节点数为：', tree.node_count(tree.root))
    print('二叉树的第三层节点数为：', tree.kth_node_count(tree.root, 3))
