# coding=utf-8
from functools import reduce


# 闭包
# def outer_func():
#     a = 1
#     def inner_func(b):
#         nonlocal a
#         a += b
#         print(a)
#         return a
#     return inner_func
#
#
# func = outer_func()
# func(100)
#
# print(outer_func()(1000))


# def func_name(func):
#     def wrapper(*args, **kwargs):
#         print("func name is {}".format(func.__name__))
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @func_name
# def func_one():
#     print('this is function one')
#
#
# @func_name
# def func_two():
#     print('this is function two')
#
#
# func_one()
# func_two()


# def decorator_one(func):
#     def wrapper(*args, **kwargs):
#         print('decorator one start')
#         result = func(*args, **kwargs)
#         print('decorator one end')
#         return result
#     return wrapper
#
#
# def decorator_two(func):
#     def wrapper(*args, **kwargs):
#         print('decorator two start')
#         result = func(*args, **kwargs)
#         print('decorator two end')
#         return result
#     return wrapper
#
#
# @decorator_two
# @decorator_one
# def hello_python():
#     print('Hello Python！')
#
#
# hello_python()


# 万能装饰器
# def decorator_all(func):
#     def wrapper(*args, **kwargs):
#         print('add some coding')
#         return func(*args, **kwargs)
#     return wrapper


# 类装饰器
class DecoratorClass(object):

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('class decorator')
        return self._func(*args, **kwargs)


@DecoratorClass
def func_three():
    print('this is function three')


func_three()
