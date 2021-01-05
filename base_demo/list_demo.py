# coding=utf-8
# list_a = list()
# for a in range(5):
#     list_a.append(a)
# print(list_a)
#
# list_b = [b for b in range(5)]
# print(list_b)


# # in后面跟其他可迭代对象,如字符串
# list_c = [7 * c for c in "python"]
# print(list_c)

# # 带if条件语句的列表推导式
# list_d = [d for d in range(6) if d % 2 != 0]
# print(list_d)

# # 多个for循环
# list_e = [(e, f * f) for e in range(3) for f in range(5, 15, 5)]
# print(list_e)

# # 嵌套列表推导式,多个并列条件
# list_g = [[x for x in range(g - 3, g)] for g in range(22) if g % 3 == 0 and g != 0]
# print(list_g)


# 因为key是唯一的,所以最后value都是1
# dict_a = {key: value for key in 'python' for value in range(2)}
# print(dict_a)

# 可以根据键来构造值
# dict_b = {key: key * key for key in range(6)}
# print(dict_b)

# 遍历一个有键值关系的可迭代对象
# list_phone = [('HUAWEI', '华为'), ('MI', '小米'), ('OPPO', 'OPPO'), ('VIVO', 'VIVO')]
# dict_c = {key: value for key, value in list_phone}
# print(dict_c)


# # 遍历一个可迭代对象生成集合
# set_a = {value for value in '有人云淡风轻,有人负重前行'}
# print(set_a)
