# coding=utf-8

# # 新建一个文件，文件名为:file_a.txt,用于写入内容
# f = open('file_a.txt', 'w')
#
# # 关闭这个文件
# f.close()


# f = open('file_b.txt', 'w')
# # 写入内容
# f.write('当我和拥挤的人群一同在路上走过时，\n我看见您从阳台上送过来的微笑，\n我歌唱着，\n忘却了所有的喧哗')
# f.close()


# f = open('file_b.txt', 'r')
# # 读取
# content = f.read(15)
# content_all = f.read()
# print('content: ', content)
# print('content_all: ', content_all)
# f.close()


# with open('file_b.txt', 'r') as f:
#     content_list = f.readlines()
#     print('content_list: ', content_list)
#
#
# with open('file_b.txt', 'r') as f:
#     content_line1 = f.readline()
#     print('content_line1: ', content_line1)
#     content_line2 = f.readline()
#     print('content_line2: ', content_line2)


# with open('file_b.txt', 'r') as f:
#     content_line = f.readline()
#     # 获取当前位置
#     position = f.tell()
#     print(position)


# with open('file_b.txt', 'r') as f:
#     position = f.tell()
#     print(position)
#     f.seek(10, 0)
#     position = f.tell()
#     print(position)


import os

# os.rename("file_b.txt", "file_c.txt")

# os.remove("file_a.txt")

# os.mkdir("files")

# print(os.getcwd())

# os.chdir("files")

# print(os.listdir())

os.rmdir("files")
