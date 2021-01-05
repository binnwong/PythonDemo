# coding=utf-8
# class Electrical(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def watch_movie(self):
#         print('Watch movie!')
#
#     def game(self):
#         print('Play game!')
#
#     def chat(self):
#         print('Chat with friend!')
#
#
# class Phone(Electrical, object):
#
#     def send_message(self):
#         print('Send message!')
#
#     def game(self):
#         print('Play game in phone!')
#
#     def chat(self):
#         super(Phone, self).chat()
#         print('Chat with anyone!')


# p = Phone('VIVO')
# # 继承父类的属性
# print(p.name)
# # 继承父类的方法
# p.watch_movie()
# # 子类自己实现的方法
# p.send_message()
# # 重写了父类的方法
# p.game()
# # 先继承父类的方法，在对父类方法的功能进行扩展
# p.chat()


# class Mi(Phone):
#     pass
#
#
# m = Mi('Redmi')
# print(m.name)
# m.chat()


# class Computer(Electrical):
#
#     def coding(self):
#         print('Coding something!')
#
#
# class HuaWei(Phone, Computer):
#     pass
#
#
# h = HuaWei('huawei')
# h.send_message()
# h.coding()
# print(h.name)
# h.watch_movie()
