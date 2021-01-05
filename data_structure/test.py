# coding=utf-8
def pprint(self, *args, sep=' ', end='\n', file=None, pre=None):
    if pre is not None:
        print(pre, end='')
    print(self, *args, sep=' ', end='\n', file=None)


if __name__ == '__main__':
    # pprint('ABCD')
    # pprint('ABCD', pre='\n')
    l = [23, 45, 11, 3, 44, 6, 22, 10, 44, 2, 33, 55, 6, 7]
    # m1, m2 = l[0], l[1]
    # for i in l:
    #     if m1 > m2:
    #         m1, m2 = m2, m1
    #     if i < m1:
    #         m1, m2 = i, m1
    # print(m1, m2)
    # print(max(l))
    l.remove(6)
    print(l)
    # print(\033[显示方式;前景色;背景色m输出内容\033[0m)
    print('aaaa' + "\033[31m{}\033[0m".format(10))
    print("\033[30m10\033[0m")


