# coding=utf-8
from functools import reduce


# def sum_func(a, b, c):
#     return a + b + c
#
#
# sum_lambda = lambda a, b, c: a + b + c
#
# print(sum_func(1, 100, 10000))
# print(sum_lambda(1, 100, 10000))


# # 无参数
# lambda_a = lambda: 100
# print(lambda_a())
#
# # 一个参数
# lambda_b = lambda num: num * 10
# print(lambda_b(5))
#
# # 多个参数
# lambda_c = lambda a, b, c, d: a + b + c + d
# print(lambda_c(1, 2, 3, 4))
#
# # 表达式分支
# lambda_d = lambda x: x if x % 2 == 0 else x + 1
# print(lambda_d(6))
# print(lambda_d(7))


# def sub_func(a, b, func):
#     print('a =', a)
#     print('b =', b)
#     print('a - b =', func(a, b))
#
#
# sub_func(100, 1, lambda a, b: a - b)


member_list = [
    {"name": "风清扬", "age": 99, "power": 10000},
    {"name": "无崖子", "age": 89, "power": 9000},
    {"name": "王重阳", "age": 120, "power": 8000}
]
new_list = sorted(member_list, key=lambda dict_: dict_["power"])
print(new_list)


number_list = [100, 77, 69, 31, 44, 56]
num_sum = list(map(lambda x: {str(x): x}, number_list))
print(num_sum)


def run_func(a, b):
    return lambda c: a + b + c


return_func = run_func(1, 10000)
print(return_func)
print(return_func(100))
