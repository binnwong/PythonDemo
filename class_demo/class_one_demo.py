# coding=utf-8


# class Custom(object):
#
#     def __init__(self, name, money):
#         self.name = name
#         self.__money = money
#
#
# c = Custom('tom', 100)
# print(c.name)
# print(c.__money)


# class Custom(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def get_money(self):
#         return self.__money
#
#     def set_money(self, money):
#         if money > 0:
#             self.__money = money
#         else:
#             self.__money = 0
#             print('参数值错误！')
#
#
# c = Custom('tom')
# print(c.name)
# c.name = 'TOM'
# print(c.name)
# c.set_money(-100)
# c.set_money(100)
# print(c.get_money())


# class Interviewer(object):
#
#     def __init__(self):
#         self.wage = 0
#
#     def ask_question(self):
#         print('ask some question!')
#
#     def __talk_wage(self):
#         print('Calculate wage !')
#
#     def talk_wage(self):
#         if self.wage > 20000:
#             print('too high ！')
#         else:
#             self.__talk_wage()
#             print('welcome to join us!')
#
#
# me = Interviewer()
# me.ask_question()
# # me.__talk_wage()
# me.wage = 30000
# me.talk_wage()
# print('-' * 20)
# me.wage = 15000
# me.talk_wage()


# class Father(object):
#
#     def __init__(self):
#         self.home = 'China'
#         self.__house = 'house'
#
#     def make_money(self):
#         print('make money')
#
#     def __project(self):
#         print('project work')
#
#
# class Son(Father):
#
#
#     def work(self):
#         print('work like a dog!')
#
#
# s = Son()
# print(s.home)
# # print(s.__house)
# s.work()
# s.make_money()
# # s.__project()

a = 1
_a = 10
__a = 100


def func():
    print(a)
    print(_a)
    print(__a)


func()


def func2():
    _b = 10
    __b = 100
    print(_b)
    print(__b)


_b = 1000
func2()
