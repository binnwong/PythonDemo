# # coding=utf-8
# import copy
#
#
# base = ['a', 'b', 'c', 'd', 'e']
# # 切片
# bak1 = base[:]
# print("bak1: ", bak1)
# # list工厂函数
# bak2 = list(base)
# print("bak2: ", bak2)
# # python list对象的copy方法
# bak3 = base.copy()
# print("bak3: ", bak3)
# # copy模块的copy方法
# bak4 = copy.copy(base)
# print("bak4: ", bak4)


import copy

son = ['python', 'copy']
base = ['a', 'b', 'c', 'd', 'e', son]
bak1 = base[:]
print("bak1: ", bak1)
bak2 = list(base)
print("bak2: ", bak2)
bak3 = base.copy()
print("bak3: ", bak3)
bak4 = copy.copy(base)
print("bak4: ", bak4)
print('-' * 20, '分割线', '-' * 20)
son[0] = 'PYTHON'
son[1] = 'COPY'
print('base: ', base)
print("bak1: ", bak1)
print("bak2: ", bak2)
print("bak3: ", bak3)
print("bak4: ", bak4)


# a = 'a'
# print(id(a))
# a = 'b'
# print(id(a))


# base = [1, 2, 3]
# print(id(base))
# base[0] = 100
# print(base)
# print(id(base))


# list_a = [1, 2, 3]
# list_a[2] = 30
# print('list_a: ', list_a)


# list_b = [1, 2, 3]
# list_c = list_b.copy()
# print('list_c: ', list_c)


# import copy
#
#
# list_b = [1, 2, 3]
# list_c = copy.copy(list_b)
# list_b[2] = 30
# print('list_b: ', list_b)
# print('list_c: ', list_c)


# import copy
#
#
# sub = [2, 3]
# list_d = [1, sub]
# list_e = copy.copy(list_d)
# print('list_d: ', list_d)
# print('list_e: ', list_e)


# import copy
#
#
# sub = [2, 3]
# list_d = [1, sub]
# list_e = copy.copy(list_d)
# list_d[1][1] = 30
# print('list_d: ', list_d)
# print('list_e: ', list_e)


# import copy
#
#
# sub = [2, 3]
# list_d = [1, sub]
# list_f = copy.deepcopy(list_d)
# list_d[1][1] = 30
# print('list_d: ', list_d)
# print('list_e: ', list_f)
