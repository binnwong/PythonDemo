# coding=utf-8
class RBNode(object):
    """节点类"""
    def __init__(self, data, left_child=None, right_child=None, color='red'):
        self.data = data
        self.parent = None
        self.left_child = left_child
        self.right_child = right_child
        self.color = color


class RBBinaryTree(object):
    """红黑树类"""
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
        self.__root = value if isinstance(value, RBNode) else RBNode(value)

    def left_rotate(self, node):
        """红黑树左旋"""
        parent_node, right_node = node.parent, node.right_child
        if not right_node:
            return
        # 1.node是旋转节点，将旋转节点的右子节点的左子节点变为旋转节点的右子节点
        node.right_child = right_node.left_child
        if node.right_child:
            node.right_child.parent = node
        # 2.将旋转节点修改为右子节点的左子节点
        right_node.left_child, node.parent = node, right_node
        # 3.将右子节点替换旋转节点的位置，作为旋转节点父节点的子节点
        if not parent_node:
            self.root = right_node
        else:
            if parent_node.left_child == node:
                parent_node.left_child = right_node
            else:
                parent_node.right_child = right_node
        right_node.parent = parent_node

    def right_rotate(self, node):
        """红黑树右旋"""
        parent_node, left_node = node.parent, node.left_child
        if not left_node:
            return
        # 1.node是旋转节点，将旋转节点的左子节点的右子节点变为旋转节点的左子节点
        node.left_child = left_node.right_child
        if node.left_child:
            node.left_child.parent = node
        # 2.将旋转节点修改为左子节点的右子节点
        left_node.right_child, node.parent = node, left_node
        # 3.将左子节点替换旋转节点的位置，作为旋转节点父节点的子节点
        if not parent_node:
            self.root = left_node
        else:
            if parent_node.left_child == node:
                parent_node.left_child = left_node
            else:
                parent_node.right_child = left_node
        left_node.parent = parent_node

    def change_color(self, node):
        """红黑树变色"""
        if node.color is 'red':
            node.color = 'black'
        elif node.color is 'black':
            node.color = 'red'

    def rb_insert(self, value):
        """红黑树插入"""
        node = value if isinstance(value, RBNode) else RBNode(value)
        if self.search(self.root, node.data):
            return
        if self.is_empty():
            node.color = 'black'
            self.root = node
            return
        self.insert(self.root, node)
        factor_node = node
        while True:
            parent_node = factor_node.parent
            if parent_node.color is 'red':
                grandparent_node = parent_node.parent
                if parent_node is grandparent_node.left_child:
                    uncle_node = grandparent_node.right_child
                else:
                    uncle_node = grandparent_node.left_child
                # 如果父节点为红节点且叔节点为黑节点
                if uncle_node is None or uncle_node and uncle_node.color is 'black':
                    if parent_node == grandparent_node.left_child:
                        # 先左旋为左左结果，然后父节点和祖父节点变色，再右旋
                        if factor_node == parent_node.right_child:
                            self.left_rotate(parent_node)
                            self.change_color(factor_node)
                        else:
                            self.change_color(parent_node)
                        self.change_color(grandparent_node)
                        self.right_rotate(grandparent_node)
                    elif parent_node == grandparent_node.right_child:
                        # 先右旋为右右结构，然后父节点和祖父节点变色，再左旋
                        if factor_node == parent_node.left_child:
                            self.right_rotate(parent_node)
                            self.change_color(factor_node)
                        else:
                            self.change_color(parent_node)
                        self.change_color(grandparent_node)
                        self.left_rotate(grandparent_node)
                    break
                # 如果父节点为红节点且叔节点也为红节点
                elif uncle_node and uncle_node.color is 'red':
                    # 父节点和叔节点变色，祖父节点变色(祖父节点是根节点除外)
                    self.change_color(parent_node)
                    self.change_color(uncle_node)
                    if grandparent_node != self.root:
                        self.change_color(grandparent_node)
                        # 祖父节点变成红节点后，将祖父节点作为新的因素节点，判断其父节点，避免不满足特性4
                        factor_node = grandparent_node
            else:
                break

    def insert(self, root, value):
        """二叉搜索树插入节点-递归"""
        node = value if isinstance(value, RBNode) else RBNode(value)
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

    def show_tree(self):
        if self.is_empty():
            print('空二叉树')
            return
        print('-' * 20)
        print("\033[31m{}\033[0m".format(str(self.root.data))) if self.root.color is 'red' else print(str(self.root.data))
        self.__print_tree(self.__root)
        print('-' * 20)

    def __print_tree(self, node, prefix=None):
        if prefix is None:
            prefix, prefix_left_child = '', ''
        else:
            prefix = prefix.replace(self.prefix_branch, self.prefix_trunk).replace(self.prefix_leaf, self.prefix_empty)
            prefix_left_child = prefix.replace(self.prefix_leaf, self.prefix_empty)
        if self.has_child(node):
            if node.right_child is not None:
                if node.right_child.color is 'red':
                    print(prefix + self.prefix_branch + self.prefix_right + "\033[31m{}\033[0m".format(str(node.right_child.data)))
                else:
                    print(prefix + self.prefix_branch + self.prefix_right + str(node.right_child.data))
                if self.has_child(node.right_child):
                    self.__print_tree(node.right_child, prefix + self.prefix_branch + ' ')
            else:
                print(prefix + self.prefix_branch + self.prefix_right)
            if node.left_child is not None:
                if node.left_child.color is 'red':
                    print(prefix + self.prefix_leaf + self.prefix_left + "\033[31m{}\033[0m".format(str(node.left_child.data)))
                else:
                    print(prefix + self.prefix_leaf + self.prefix_left + str(node.left_child.data))
                if self.has_child(node.left_child):
                    prefix_left_child += '  '
                    self.__print_tree(node.left_child, self.prefix_leaf + prefix_left_child)
            else:
                print(prefix + self.prefix_leaf + self.prefix_left)

    def has_child(self, node):
        return node.left_child is not None or node.right_child is not None


if __name__ == '__main__':
    tree = RBBinaryTree()
    data = [50, 77, 55, 29, 10, 30, 66, 18, 80, 51, 90]
    for i in data:
        # tree.insert(tree.root, i)
        tree.rb_insert(i)
    tree.show_tree()

    # node = tree.search(tree.root, 77)
    # tree.left_rotate(node)
    # tree.show_tree()

    # node = tree.search(tree.root, 80)
    # tree.right_rotate(node)
    # tree.show_tree()

    # tree.change_color(tree.search(tree.root, 50))
    # tree.change_color(tree.search(tree.root, 10))
    # tree.show_tree()
