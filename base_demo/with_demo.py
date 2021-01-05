# with open('test.txt', 'a') as f:
#     f.write('上下文管理\n')


# class OpenFile(object):
#     """自定义上下文管理类"""
#
#     def __init__(self, file, mode):
#         self._file = file
#         self._mode = mode
#
#     def __enter__(self):
#         print('__enter__  打开文件')
#         self._handle = open(self._file, self._mode)
#         return self._handle
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('__exit__ 关闭文件')
#         self._handle.close()
#
#
# with OpenFile('test01.txt', 'w') as f:
#     f.write('自定义上下文管理\n')


# class OpenFile(object):
#     """自定义上下文管理类"""
#
#     def __init__(self, file, mode):
#         self._file = file
#         self._mode = mode
#
#     def __enter__(self):
#         self._handle = open(self._file, self._mode)
#         return self._handle
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Type: ', exc_type)
#         print('Value:', exc_val)
#         print('TreacBack:', exc_tb)
#         self._handle.close()
#
#
# with OpenFile('test01.txt', 'r') as f:
#     f.write('自定义上下文管理\n')


class OpenFile(object):
    """自定义上下文管理类"""

    def __init__(self, file, mode):
        self._file = file
        self._mode = mode

    def __enter__(self):
        self._handle = open(self._file, self._mode)
        return self._handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._handle.close()
        # 通过exc_type参数接收到的值，来判断程序执行是否出现异常
        # 如果是None,说明没有异常
        if exc_type == "None":
            print('正常执行')
        else:
            # 否则出现异常，可以选择怎么处理异常
            print(exc_type, exc_val)
        # 返回值决定了捕获的异常是否继续向外抛出
        # 如果是False那么就会继续向外抛出，程序会看到系统提示的异常信息
        # 如果是True不会向外抛出,程序看不到系统提示信息，只能看到else中的输出
        return True


with OpenFile('test01.txt', 'r') as f:
    f.write('自定义上下文管理\n')
