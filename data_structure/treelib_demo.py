# coding=utf-8
from treelib import Tree, Node


tree = Tree()
tree.show()
print(tree.identifier)



tree.create_node(tag='Node-5', identifier='node-5', data=5)
tree.create_node(tag='Node-10', identifier='node-10', parent='node-5', data=10)
tree.create_node('Node-15', 'node-15', 'node-10', 15)
# tree.show()

node = Node(data=50)
tree.add_node(node, parent='node-5')
node_a = Node(tag='Node-A', identifier='node-A', data='A')
tree.add_node(node_a, parent='node-5')
# tree.show()


# print(node)
# print('node id: ', node.identifier)
# print('node tag:', node.tag)
# print('node data:', node.data)
#
# print('node is leaf: ', node.is_leaf())
# print('node is root: ', node.is_root())


# tree1 = Tree(tree=tree, deep=True)
# tree1.create_node('Node-16', 'node-16', 'node-10', 16)
# tree1.show()
# tree.show()


# tree.show()
# 返回树中的节点个数
# print('tree len: ', len(tree))
# print('tree size:', tree.size())
tree.create_node(tag='Node-20', identifier='node-20', parent='node-10', data=20)
tree.create_node(tag='Node-30', identifier='node-30', parent='node-15', data=30)
# 返回指定深度(level)节点个数，若无指定则返回整棵树节点个数
# print('tree size:', tree.size())


# tree.show()
# # 返回所有节点，是一个列表
# print(tree.all_nodes())
# # 返回所有节点，是一个可迭代器
# for node in tree.all_nodes_itr():
#     print(node)
# # 返回一个生成器，id
# for id in tree.expand_tree():
#     print(id)


# # 返回节点的子节点
# print('node-5 children:', tree.children('node-5'))
# # 返回节点的所有子节点id
# print('node-10 branch:', tree.is_branch('node-10'))
# # 返回节点的兄弟节点，列表
# print('node-20 siblings:', tree.siblings('node-20'))
# # 返回节点的父节点
# print('node-30 parent:', tree.parent('node-30'))
# # 返回节点的祖先
# print('node-15 ancestor: ', tree.ancestor('node-15'))
# # 返回a是不是b的祖先
# print(tree.is_ancestor('node-15', 'node-30'))
# # 遍历节点到根的路径,返回一个生成器
# for node in tree.rsearch('node-30'):
#     print(node)


# # 返回树的深度，指定节点则返回节点的深度
# print('tree depth:', tree.depth())
# print('node-20 depth:', tree.depth(node='node-20'))
# # 返回指定节点在树中的高度
# print('node-20 level:', tree.level('node-20'))
# # 返回所有叶节点
# print('tree leaves:', tree.leaves())
# # 返回根节点到每个叶节点的路径上的节点，列表嵌套列表
# print(tree.paths_to_leaves())


# # 返回节点是否在树中
# print('node-10 is in tree:', tree.contains('node-10'))
# print('node-100 is in tree:', tree.contains('node-100'))
# # 从树中获取节点，节点不存在则返回None
# print(tree.get_node('node-10'))
# print(tree.get_node('node-100'))
# # 更新节点的属性
# tree.update_node('node-20', data=200)
# print('data of node-20:', tree.get_node('node-20').data)


# 将节点子节点链接到其父节点上，将节点删除
# tree.show()
tree.link_past_node('node-10')
# tree.show()
# 将source节点移动成destination的子节点
tree.move_node('node-30', 'node-20')
# tree.show()


tree2 = Tree()
tree2.create_node(tag='Node-7', identifier='node-7', data=7)
tree2.create_node(tag='Node-17', identifier='node-17', parent='node-7', data=17)
# tree2.show()
# 将一颗树粘贴成nid的子树
tree.paste('node-20', tree2)
# tree.show()

tree3 = Tree()
tree3.create_node(tag='Node-8', identifier='node-8', data=8)
tree3.create_node(tag='Node-18', identifier='node-18', parent='node-8', data=18)
# tree3.show()
# 将新树合并到指定的节点，新树的根节点不保留
tree.merge('node-A', tree3)
# tree.show()
# 浅拷贝子树
print(tree.subtree('node-20'))


# print(tree.to_dict())
# print(tree.to_json())
# tree.to_graphviz()
# 将当前树保持到指定文件中
# tree.save2file('demo_tree.tree')


tree.show()
# 删除节点及其子节点,返回删除的节点个数
print('remover node: ', tree.remove_node('node-7'))
tree.show()
# 删除以节点为根节点的子树，返回子树
print(tree.remove_subtree('node-20'))
tree.show()
