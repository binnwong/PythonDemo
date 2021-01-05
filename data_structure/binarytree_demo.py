# coding=utf-8
from binarytree import *


# tree0 = tree()
# print('tree0:', tree0)
# tree1 = tree(height=2, is_perfect=True)
# print('tree1:', tree1)
# tree2 = tree(height=2, is_perfect=False)
# print('tree2:', tree2)


# bst0 = bst()
# print('bst0:', bst0)
# bst1 = bst(height=3, is_perfect=True)
# print('bst1:', bst1)
# bst2 = bst(height=2, is_perfect=False)
# print('bst2:', bst2)


# heap0 = heap()
# print('heap0:', heap0)
# heap1 = heap(height=2, is_max=True, is_perfect=True)
# print('heap1:', heap1)
# heap2 = heap(height=2, is_max=False, is_perfect=True)
# print('heap2:', heap2)
# heap3 = heap(height=2, is_max=False, is_perfect=False)
# print('heap3:', heap3)


# values = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
# build_tree = build(values)
# print(build_tree)
# print(build_tree.values)


# values = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
# build_tree = build(values)
# print(build_tree)
# child_node = build_tree.left.right
# print('child_node: ', child_node.value)
# parent = get_parent(build_tree, child_node)
# print('parent_node: ', parent.value)
# parent = get_parent(build_tree, build_tree)
# print('parent_node: ', parent)


# root = Node(10)
# root.left = Node(5)
# root.right = Node(15)
# print(root)

data = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
nodes = [None if i is None else Node(i) for i in data]
root = nodes[0]
root.left = nodes[1]
root.right = nodes[2]
root.left.left = nodes[3]
root.left.right = nodes[4]
root.right.left = nodes[5]
root.right.right = nodes[6]
root.pprint()
print('层序遍历： ', root.levelorder)
print('先序遍历： ', root.preorder)
print('中序遍历： ', root.inorder)
print('后序遍历： ', root.postorder)

#
# print(dir(root))
# print(root.properties)



