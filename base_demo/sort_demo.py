# coding=utf-8
# list_a = [1, 2, 8, 3, 7, 9, 5, 7]
# # sort()方法没有返回值
# list_b = list_a.sort()
# print("list_a: ", list_a)
# print('list_b: ', list_b)


# list_c = [1, 2, 8, 3, 7, 9, 5, 7]
# # sorted内置函数会返回一个排序后的新列表
# list_d = sorted(list_c)
# print("list_c: ", list_c)
# print('list_d: ', list_d)


# # 可以非列表的可迭代对象排序生成列表
# str_e = 'python'
# list_e = sorted(str_e)
# print(list_e)
#
# # 链式调用
# str_f = '-'.join(sorted(str_e)).upper().split('-')
# print(str_f)


phone = ('HUAWEI', 'OPPO', 'MI', 'MEIZU', 'VIVO')
# 按长度进行排序
phone_list = sorted(phone, key=len)
print(phone_list)

phone_list_re = sorted(phone, key=len, reverse=True)
print(phone_list_re)
