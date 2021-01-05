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

    def rb_delete(self, value):
        """红黑树删除"""
        if not self.is_empty():
            node_delete = self.search(self.root, value)
            if node_delete:
                self._rb_delete(node_delete)
            else:
                raise KeyError("Error, {value} not in this tree".format(value=value))
        else:
            raise KeyError("Error, tree is empty")

    def _rb_delete(self, node):
        """删除节点的三种情况"""
        if node.left_child is None and node.right_child is None:
            self._rb_delete_no_child(node)
        elif node.left_child and not node.right_child or not node.left_child and node.right_child:
            self._rb_delete_one_child(node)
        else:
            rear_node = self.get_min(node.right_child)
            node.data = rear_node.data
            self._rb_delete(rear_node)

    def _rb_delete_no_child(self, node):
        """红黑树删除两个子节点都为空的节点"""
        if node == self.root:
            self.root = None
            self.root.color = 'black'
            return
        factor_node = node
        # 如果待删除节点为黑节点则需要进行调整
        if factor_node.color is 'black':
            while True:
                parent_node = factor_node.parent
                brother_node = parent_node.right_child if factor_node is parent_node.left_child else parent_node.left_child
                # 待删除节点是左子节点
                if factor_node is parent_node.left_child:
                    # 如果兄弟节点是黑节点
                    if brother_node.color is 'black':
                        # 如果兄弟节点没有子节点(递归处理时如果兄弟节点的两个子节点都是黑节点)
                        if brother_node.left_child is None and brother_node.right_child is None or \
                        ((brother_node.left_child and brother_node.left_child.color is 'black') and
                        (brother_node.right_child and brother_node.right_child.color is 'black')):
                            self.change_color(brother_node)
                            if parent_node.color is 'red':
                                self.change_color(parent_node)
                                break
                            else:
                                if parent_node == self.root:
                                    break
                                factor_node = parent_node
                        # 如果兄弟节点有右子节点，此右节点一定是红节点(递归处理时，如果兄弟节点的右子节点为红节点)
                        elif brother_node.right_child is not None and brother_node.right_child.color is 'red':
                            brother_node.color = parent_node.color
                            parent_node.color, brother_node.right_child.color = 'black', 'black'
                            self.left_rotate(parent_node)
                            break
                        # 如果兄弟节点有左节点，此左节点一定是红节点(递归处理时，如果兄弟节点的左子节点为红节点)
                        else:
                            brother_node.color, brother_node.left_child.color = 'red', 'black'
                            self.right_rotate(brother_node)
                    # 如果兄弟节点是红节点
                    elif brother_node.color is 'red':
                        self.change_color(parent_node)
                        self.change_color(brother_node)
                        self.left_rotate(parent_node)
                # 待删除节点是右子节点
                if factor_node is parent_node.right_child:
                    if brother_node.color is 'black':
                        # 如果兄弟节点没有子节点(递归处理时如果兄弟节点的两个子节点都是黑节点)
                        if brother_node.left_child is None and brother_node.right_child is None or \
                        ((brother_node.left_child and brother_node.left_child.color is 'black') and
                        (brother_node.right_child and brother_node.right_child.color is 'black')):
                            self.change_color(brother_node)
                            if parent_node.color is 'red':
                                self.change_color(parent_node)
                                break
                            else:
                                if parent_node == self.root:
                                    break
                                factor_node = parent_node
                        # 如果兄弟节点有左节点，此左节点一定是红节点(递归处理时，如果兄弟节点的左子节点为红节点)
                        elif brother_node.left_child is not None and brother_node.left_child.color is 'red':
                            brother_node.color = parent_node.color
                            parent_node.color, brother_node.left_child.color = 'black', 'black'
                            self.right_rotate(parent_node)
                            break
                        # 如果兄弟节点有右节点，此右节点一定是红节点(递归处理时，如果兄弟节点的右子节点为红节点)
                        else:
                            brother_node.color, brother_node.right_child.color = 'red', 'black'
                            self.left_rotate(brother_node)
                    # 如果兄弟节点是红节点
                    elif brother_node.color is 'red':
                        self.change_color(parent_node)
                        self.change_color(brother_node)
                        self.right_rotate(parent_node)
        if node is node.parent.left_child:
            node.parent.left_child = None
        else:
            node.parent.right_child = None
        node.parent = None

    def _rb_delete_one_child(self, node):
        """红黑树删除有一个子节点的节点"""
        if node.left_child:
            self.change_color(node.left_child)
            if node.parent and node.parent.left_child == node:
                node.left_child.parent, node.parent.left_child = node.parent, node.left_child
            elif node.parent and node.parent.right_child == node:
                node.left_child.parent, node.parent.right_child = node.parent, node.left_child
            else:
                self.root = node.left_child
                node.left_child.parent, node.left_child = None, None
        elif node.right_child:
            self.change_color(node.right_child)
            if node.parent and node.parent.left_child == node:
                node.right_child.parent, node.parent.left_child = node.parent, node.right_child
            elif node.parent and node.parent.right_child == node:
                node.right_child.parent, node.parent.right_child = node.parent, node.right_child
            else:
                self.root = node.right_child
                node.right_child.parent, node.right_child = None, None
        node.parent = None

    def rb_check(self):
        """检查红黑树是否满足5条特性"""
        if self.is_empty():
            print("空树")
            return
        queue = list()
        queue.insert(0, self.root)
        height = 0
        while len(queue):
            node = queue.pop()
            if node.color is not "red" and node.color is not "black":
                raise Exception("节点{}不满足特性1".format(node.data))
            if node is self.root and node.color is not "black":
                raise Exception("节点{}不满足特性2".format(node.data))
            if node.color is "red" and (node.left_child and node.left_child.color is "red" or
                                        node.right_child and node.right_child.color is "red"):
                raise Exception("节点{}不满足特性4".format(node.data))
            if node.left_child is None and node.right_child is None:
                path = 0
                cur = node
                while cur:
                    if cur.color is "black":
                        path += 1
                    cur = cur.parent
                if height and path != height:
                    raise Exception("节点{}不满足特性5".format(node.data))
                else:
                    height = path
            if node.left_child is not None:
                queue.insert(0, node.left_child)
            if node.right_child is not None:
                queue.insert(0, node.right_child)
        print("满足红黑树的5条特性,叶子节点到根节点的非空黑节点个数为{}".format(height))

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

    def get_min(self, root):
        """查找二叉搜索树值最小的节点"""
        if self.is_empty():
            return
        return self.get_min(root.left_child) if root.left_child else root

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
    # data = [50, 77, 55, 29, 10, 30, 66, 18, 80, 51, 90]
    # for i in data:
    #     tree.rb_insert(i)
    # # tree.show_tree()
    #
    # tree.rb_delete(66)
    # tree.show_tree()

    data = range(1000)
    for i in data:
        tree.rb_insert(i)
    tree.rb_check()
    tree.rb_delete(66)
    print("--- after delete ---")
    tree.rb_check()
