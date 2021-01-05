# coding=utf-8
class Node(object):
    """节点类"""
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.parent = None
        self.left_child = left_child
        self.right_child = right_child


class SearchBinaryTree(object):
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
    def root(self, value):
        self.__root = value if isinstance(value, Node) else Node(value)

    def show_tree(self):
        if self.is_empty():
            print('空二叉树')
            return
        print('-' * 20)
        print(self.__root.data)
        self.__print_tree(self.__root)
        print('-' * 20)

    def insert(self, root, value):
        """二叉搜索树插入节点-递归"""
        node = value if isinstance(value, Node) else Node(value)
        if self.is_empty():
            self.root = node
            return
        if root is None:
            root = node
        elif node.data < root.data:
            root.left_child = self.insert(root.left_child, value)
            root.left_child.parent = root
        elif node.data > root.data:
            root.right_child = self.insert(root.right_child, value)
            root.right_child.parent = root
        return root

    def delete(self, value):
        """二叉搜索树删除节点"""
        if self.height(self.root) >= 1:
            node_delete = self.search(self.root, value)
            if node_delete:
                self._delete(node_delete)
            else:
                raise KeyError("Error, value not in this tree")
        else:
            raise KeyError("Error, value not in this tree")

    def _delete(self, node):
        """删除节点"""
        if not node.left_child and not node.right_child:
            self._delete_no_child(node)
        elif node.left_child and not node.right_child or not node.left_child and node.right_child:
            self._delete_one_child(node)
        else:
            rear_node = self.get_min(node.right_child)
            node.data = rear_node.data
            self._delete(rear_node)

    def _delete_no_child(self, node):
        """删除叶节点"""
        if node == self.root:
            self.root = None
            return
        if node == node.parent.left_child:
            node.parent.left_child = None
        else:
            node.parent.right_child = None
        node.parent = None

    def _delete_one_child(self, node):
        """删除有一个子节点的节点"""
        if node.left_child:
            if node.parent and node.parent.left_child == node:
                node.left_child.parent = node.parent
                node.parent.left_child = node.left_child
            elif node.parent and node.parent.right_child == node:
                node.left_child.parent = node.parent
                node.parent.right_child = node.left_child
            else:
                self.root = node.left_child
                node.left_child.parent = None
                node.left_child = None
        else:
            if node.parent and node.parent.left_child == node:
                node.right_child.parent = node.parent
                node.parent.left_child = node.right_child
            elif node.parent and node.parent.right_child == node:
                node.right_child.parent = node.parent
                node.parent.right_child = node.right_child
            else:
                self.root = node.right_child
                node.right_child.parent = None
                node.right_child = None
        node.left_child = None
        node.parent = None

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

    def search(self, root, data):
        """二叉搜索树的查询操作"""
        if root is None:
            return
        if root.data == data:
            return root
        elif data < root.data:
            return self.search(root.left_child, data)
        elif data > root.data:
            return self.search(root.right_child, data)

    def get_max(self, root):
        """查找二叉搜索树值最大的节点"""
        if self.is_empty():
            return
        return self.get_max(root.right_child) if root.right_child else root

    def get_min(self, root):
        """查找二叉搜索树值最小的节点"""
        if self.is_empty():
            return
        return self.get_min(root.left_child) if root.left_child else root

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
    tree = SearchBinaryTree()
    data = [50, 77, 55, 29, 10, 30, 66, 80, 51, 18, 90, 78, 79]
    for i in data:
        tree.insert(tree.root, i)
    # tree.show_tree()

    # node = tree.search(tree.root, 66)
    # tree._delete_no_child(node)
    # tree.show_tree()

    # node = tree.search(tree.root, 10)
    # tree._delete_one_child(node)
    # tree.show_tree()

    tree.delete(80)
    tree.show_tree()
