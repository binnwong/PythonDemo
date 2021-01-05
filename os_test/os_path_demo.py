# coding=utf-8
import os


# # 返回当前位置的绝对路径
# print(os.getcwd())
# print(os.path.abspath('..'))
# # 返回path的真实路径
# print(os.path.realpath('..'))
# # 返回从start开始计算的相对路径
# print(os.path.relpath('.', '/home/python/Desktop'))


# # 返回文件夹的名字或文件名
# print(os.path.basename('./os_path_demo.py'))
# print(os.path.basename('/home/python/Desktop/python_demo/os_test'))
# # 返回多个路径共有的最长的路径
# print(os.path.commonpath(['/home/python/Desktop/python_demo/os_test', '/home/python/Desktop/python_demo']))
# # 返回文件夹或文件所在的路径(可能会有问题)
# print(os.path.dirname('/home/python/Desktop/python_demo/os_test/os_path_demo.py'))
# # 返回路径是否存在
# print(os.path.exists('/home/python/Desktop/python_demo/os_test'))
# print(os.path.lexists('/home/python/Desktop/python_demo/os_test'))
# # 把路径中的“~”转换成用户目录(可能会有问题)
# print(os.path.expanduser('~/Desktop/python_demo/os_test'))
# # 把路径中的环境变量换成路径  env  export
# print(os.path.expandvars('${SHELL}'))


# # 返回路径是否为绝对路径(可能会有问题)
# print(os.path.isabs('Desktop/python_demo/os_test'))
# # 返回是不是文件
# print(os.path.isfile('Desktop/python_demo/os_test'))
# print(os.path.isfile('./os_path_demo.py'))
# # 返回是不是目录
# print(os.path.isdir('.'))
# print(os.path.isdir('./os_path_demo.py'))
# # 判断是不是链接
# print(os.path.islink('./os_path_demo.py'))
# # 判断是不是挂载点 df -a
# print(os.path.ismount('/dev'))


# # 把目录和文件名合成一个路径
# print(os.path.join('Desktop/python_demo/os_test', 'os_path_demo.py'))
# # 把路径切割成目录和文件名
# print(os.path.split('/home/python/Desktop/python_demo/os_test/os_path_demo.py'))
# # 返回驱动器名和路径组成的元组
# print(os.path.splitdrive('/home/python/Desktop/python_demo/os_test/os_path_demo.py'))
# # 返回路径名和扩展名（文件后缀）的元组
# print(os.path.splitext('/home/python/Desktop/python_demo/os_test/os_path_demo.py'))


# # 转换目录的大小写和斜杠,windows中
# print(os.path.normcase('Desktop/python_demo/os_test'))
# # 规范path字符串形式,windows中
# print(os.path.normpath('Desktop/python_demo/os_test'))


# # 返回最近访问时间
# print(os.path.getatime('./os_path_demo.py'))
# print(os.path.getmtime('./os_path_demo.py'))
# print(os.path.getctime('./os_path_demo.py'))
# # 返回文件的大小
# print(os.path.getsize('./os_path_demo.py'))


# # 判断目录或文件是否相同
# print(os.path.samefile('.', '/home/python/Desktop/python_demo/os_test'))
# print(os.path.samefile('os_path_demo.py', '/home/python/Desktop/python_demo/os_test/os_path_demo.py'))
# fd = os.open('os_path_demo.py', os.O_RDONLY)
# fd2 = os.open('os_path_demo.py', os.O_RDONLY)
# print(fd)
# print(fd2)
# # 判断两个文件描述符是否指向同一个文件
# print(os.path.sameopenfile(3, 4))
# stat = os.stat('os_path_demo.py')
# stat2 = os.lstat('os_path_demo.py')
# print(stat)
# print(stat2)
# # 判断两个star是否指向同一个文件
# print(os.path.samestat(stat, stat2))




