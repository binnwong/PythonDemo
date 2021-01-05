# coding=utf-8
import os


# try:
#     # 在当前目录下创建一个文件夹
#     os.mkdir('test_folder')
# except os.error:
#     pass
# # 获取当前所在目录
# print(os.getcwd())
# try:
#     # 重命名文件夹
#     os.rename('test_folder', 'os_folder')
# except os.error:
#     pass
# # 获取目录中的文件
# print(os.listdir('os_folder'))


# # 改变目录
# os.chdir('os_folder')
# print(os.getcwd())
# # 打开一个文件,返回的是文件的文件描述符
# fd = os.open('aaa.txt', os.O_CREAT|os.O_WRONLY)
# # 在文件中写入内容
# print(fd)
# os.write(fd, 'aaaaa'.encode('utf-8'))
# # 关闭文件
# os.close(fd)
# with open('aaa.txt', 'r') as f:
#     # 获取当前文件的文件描述符
#     print(f.fileno())


# os.chdir('os_folder')
# # 创建一个bbb.txt的文件
# fd = os.open('bbb.txt', os.O_RDWR|os.O_CREAT)
# # 写入内容
# os.write(fd, 'bbbbbbb'.encode('utf-8'))
# # 关闭文件
# os.close(fd)
# # 以只读方式打开
# fd = os.open('bbb.txt', os.O_RDONLY)
# # 从文件描述符fd中读取最多n个字节
# print(os.read(fd, 20).decode('utf-8'))
# os.close(fd)
# # 删除文件
# os.remove('bbb.txt')
