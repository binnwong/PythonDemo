# coding=utf-8


# class City(object):
#
#     def __init__(self):
#         self.__name = 'SZ'
#         self.__person = 1000000
#
#     def __get_name(self):
#         return self.__name
#
#     def __set_person(self, person):
#         if isinstance(person, int):
#             if person > 1000000:
#                 self.__person = person
#             else:
#                 print('输入的人数错误！')
#         else:
#             print("人数是正整数！")
#
#     def __get_person(self):
#         return self.__person
#
#     # 通过创建property的对象，将私有方法变成一个属性给外部访问
#     name = property(__get_name)
#     # 通过创建property的对象，将私有属性变成外部可以访问和修改该的属性
#     person = property(__get_person, __set_person)
#
#
# c = City()
# print(c.name)
# print(c.person)
# # name属性没有写set的相关方法，所以property对象属性在外部不能修改
# # c.name = 'GZ'
# print(c.name)
# c.person = 100000000
# print(c.person)


class City(object):

    def __init__(self):
        self.__name = 'SZ'
        self.__person = 1000000

    @property
    def name(self):
        return self.__name

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, person):
        if isinstance(person, int):
            if person > 1000000:
                self.__person = person
            else:
                print('输入的人数错误！')
        else:
            print("人数是正整数！")


c = City()
print(c.name)
print(c.person)
# name属性没有写set的相关方法，所以property对象属性在外部不能修改
# c.name = 'GZ'
print(c.name)
c.person = 100000000
print(c.person)

