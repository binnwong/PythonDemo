# coding=utf-8
# list_a = [1, 2, 3]
# for a in list_a:
#     print(a, end=' ')
#
# tuple_b = ('a', 'b', 'c')
# for b in tuple_b:
#     print(b, end=' ')
#
# str_c = 'AKQJ'
# for c in str_c:
#     print(c, end=' ')
#
# dict_d = {'BJ': '北京', 'SH': '上海', 'GZ': '广州', 'SZ': '深圳'}
# for d in dict_d:
#     print(d, end=' ')
#
# print()
#
#
# from collections.abc import Iterable
#
# print(isinstance(list_a, Iterable))


# list_b = ['ppp', 'yyy', 'ttt', 'hhh', 'ooo', 'nnn']
# iterator_b = iter(list_b)
# print(next(iterator_b))
# print(next(iterator_b))
# print(next(iterator_b))
# print(next(iterator_b))
# print(next(iterator_b))
# print(next(iterator_b))
# print(next(iterator_b))


class FeiboIterator(object):
    """斐波那契数列迭代器"""

    def __init__(self, n):
        # 斐波那数列值的个数
        self.n = n
        # 记录当前遍历的下标
        self.index = 0
        # 斐波那数列前面的两个值
        self.num1 = 0
        self.num2 = 1

    def __next__(self):
        """被next()函数调用来获取下一个数"""
        if self.index < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.index += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self


if __name__ == '__main__':
    fb = FeiboIterator(20)
    for num in fb:
        print(num, end=' ')
