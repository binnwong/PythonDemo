# coding=utf-8
# from Tree.core import Tree
# from math import radians as rad
# from PIL import Image
#
#
# def main():
#     branches = ((.5, rad(-30)), (.6, rad(30)), (.4, rad(60)))
#     tree = Tree(pos=(0, 0, 0, -500), branches=branches)
#     tree.grow(10)
#     tree.move_in_rectangle()
#     im = Image.new("RGB", tree.get_size(), (239, 239, 239))
#     tree.draw_on(im, (85, 25, 0, 128, 53, 21), (0, 62, 21), 10)
#     im.show()
#
#
# if __name__ == '__main__':
#     main()


# # coding=utf-8
# from Tree.core import Tree
# from math import radians
# from PIL import Image
#
#
# pos = [0, 0, 0, -300]
# branches = [[0.58, radians(-45)], [0.58, radians(45)]]
# tree = Tree(pos=pos, branches=branches)
# tree.grow(5)
# # print('tree age is: ', tree.age)
# tree.move_in_rectangle()
# image = Image.new("RGB", tree.get_size(), 0)
# tree.draw_on(image, (80, 20, 10, 120, 60, 30), '#003E15', 15)
# # image.show()


# # 树干的长度
# print('树干长度：', tree.length)
# # 返回指定年龄的枝干长度，默认返回树叶
# print('树叶长度：', tree.get_branch_length())
# print(tree.get_branch_length(age=1))
# # 树生长后的坐标
# print(tree.get_rectangle())


# print('树的节点数：', tree.get_node_sum())
# print(tree.get_node_sum(3))
# # 节点的坐标，每个age一个列表
# # print(tree.nodes)
# # print(tree.get_nodes())
# # print(tree.get_branches())
# delta = (10, 10, 10, 10)
# tree.move(delta)


# # coding=utf-8
# from Tree.core import Tree
# from math import radians
# from PIL import Image
#
#
# branches = [[0.7, radians(-50)], [0.45, radians(10)], [0.6, radians(30)]]
# tree = Tree(pos=(0, 0, 0, -300), branches=branches)
# tree.grow(9)
# tree.move_in_rectangle()
# image = Image.new("RGB", tree.get_size(), (250, 250, 250))
# tree.draw_on(image, (80, 20, 10, 120, 60, 30), '#003E15', 12)
# image.show()


# coding=utf-8
from Tree.core import Tree
from math import radians
from PIL import Image


tree = Tree(pos=(0, 0, 0, 100), branches=[[1.1, radians(-30)]])
tree.grow(24)
tree.move_in_rectangle()
tree.move((100, 100, 100, 100))
size = tuple([s+200 for s in tree.get_size()])
image = Image.new("RGB", size, (250, 250, 250))
tree.draw_on(image, (255, 0, 0), (255, 0, 0), 15)
image.show()
