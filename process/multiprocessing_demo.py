# coding=utf-8
from multiprocessing import Process
import time


# def coding(language):
#     """子进程要执行的代码"""
#     for i in range(5):
#         print("{} coding".format(language), end=' | ')
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     # 单进程
#     start = time.time()
#     coding('python')
#     for i in range(5):
#         print("main program", end=' | ')
#         time.sleep(1)
#     end = time.time()
#     print('\nOne process cost time:', end - start)
#
#     # 多进程
#     multi_start = time.time()
#     p = Process(target=coding, args=('python',))
#     p.start()
#     for i in range(5):
#         print("main program", end=' | ')
#         time.sleep(1)
#     multi_end = time.time()
#     print('\nMulti process cost time:', multi_end - multi_start)


str_list = ['ppp', 'yyy']


def add_str1():
    """子进程1"""
    print('In process one: ', str_list)
    for x in 'thon':
        str_list.append(x * 3)
        time.sleep(1)
        print('In process one: ', str_list)


def add_str2():
    """子进程1"""
    print('In process two: ', str_list)
    for x in 'thon':
        str_list.append(x)
        time.sleep(1)
        print('In process two: ', str_list)


if __name__ == '__main__':
    p1 = Process(target=add_str1)
    p1.start()
    p2 = Process(target=add_str2)
    p2.start()
