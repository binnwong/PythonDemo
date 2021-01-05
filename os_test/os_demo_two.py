# coding=utf-8
import os


# try:
#     os.mkdir("folder")
# except:
#     pass
# fd = os.open('folder/ccc.txt', os.O_CREAT)
# print(os.listdir('folder'))
# os.close(fd)
# try:
#     # 删除指定的空目录，如果目录非空，则抛出一个OSError异常
#     os.rmdir("folder")
# except OSError as e:
#     print(e)
# os.remove('folder/ccc.txt')
# print(os.listdir('folder'))
# try:
#     os.rmdir("folder")
#     print("删除文件夹成功")
# except OSError as e:
#     print(e)


# try:
#     # 递归创建文件夹
#     os.makedirs("folder_a/folder_aa/folder_aaa/aaa.txt")
# except:
#     pass
# try:
#     # 递归地对目录进行更名，也可以对文件进行更名
#     os.renames("folder_a/folder_aa/folder_aaa", "folder_b/folder_bb/folder_bbb")
# except:
#     pass
# try:
#     # 递归删除目录
#     os.removedirs("folder_b/folder_bb/folder_bbb/aaa.txt")
# except:
#     pass


# # os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
# folders = os.walk(os.getcwd(), topdown=False)
# for i in folders:
#     print(i)


# # 获取path指定的路径的信息
# print(os.stat(os.getcwd()))
# # 像stat(),但是没有软链接
# print(os.lstat(os.getcwd()))


# # 检验文件的权限
# print(os.access('os_folder/aaa.txt', os.F_OK))
# print(os.access('os_folder/aaa.txt', os.R_OK))
# print(os.access('os_folder/aaa.txt', os.W_OK))
# print(os.access('os_folder/aaa.txt', os.X_OK))
#
#
# import stat
#
#
# # 修改文件的权限
# os.chmod('os_folder/aaa.txt', stat.S_IRUSR)
# print(os.access('os_folder/aaa.txt', os.X_OK))
# print(os.access('os_folder/aaa.txt', os.W_OK))
# os.chmod('os_folder/aaa.txt', stat.S_IRWXU)


# # 创建硬链接，名为dst,指向参数src
# os.link(src, dst)
# # 创建一个软链接
# os.symlink()
# # 删除文件路径
# os.unlink(path)
# # 返回软连接所指向的文件
# os.readlink(path)
