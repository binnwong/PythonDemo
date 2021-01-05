# coding=utf-8
class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.is_in_tree = False


class HuffmanTree(object):
    """霍夫曼树"""
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

    def huffman(self, leavers):
        """构造霍夫曼树"""
        if len(leavers) <= 0:
            return
        if len(leavers) == 1:
            self.root = Node(leavers[0])
            return
        woods = list()
        for i in range(len(leavers)):
            woods.append(Node(leavers[i]))
        while len(woods) < 2*len(leavers) - 1:
            node1, node2 = Node(float('inf')), Node(float('inf'))
            for j in range(len(woods)):
                if node1.data > node2.data:
                    node1, node2 = node2, node1
                if woods[j].data < node1.data and woods[j].is_in_tree is False:
                    node1, node2 = woods[j], node1
                elif node1.data <= woods[j].data < node2.data and woods[j].is_in_tree is False:
                    node2 = woods[j]
            parent_node = Node(node1.data + node2.data)
            woods.append(parent_node)
            parent_node.left_child, parent_node.right_child = node1, node2
            self.root, node1.parent, node2.parent = parent_node, parent_node, parent_node
            node1.is_in_tree, node2.is_in_tree = True, True

    def show_tree(self):
        if self.is_empty():
            print('空二叉树')
            return
        print('-' * 20)
        print(self.__root.data)
        self.__print_tree(self.__root)
        print('-' * 20)

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


if __name__ == '__main__':
    tree = HuffmanTree()
    leavers = [11, 5, 7, 13, 17, 11]
    tree.huffman(leavers)
    tree.show_tree()
