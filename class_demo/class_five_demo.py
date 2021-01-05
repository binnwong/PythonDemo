# coding=utf-8
# class Job(object):
#     pass
#
#
# j = Job()
# print(j)
# print(j.__class__)
# print(Job)
# print(Job.__class__)
# print(type(Job))


# str_a = 'python'
# str_b = str('python')
# print('str_a', str_a)
# print('str_a', str_a.__class__)
# print('str_a', str.__class__)
# print('str_b', str_b)
# print('str_b', str_b.__class__)
# print('str_b', str.__class__)
#
# print('-' * 20)
# list_a = [x for x in range(5)]
# list_b = list([x for x in range(5)])
# print('list_a', list_a)
# print('list_a', list_a.__class__)
# print('list_a', list.__class__)
# print('list_b', list_b)
# print('list_b', list_b.__class__)
# print('list_b', list.__class__)


# print(object.__class__)
# print(type.__class__)
#
# print(type.__mro__)
# print(object.__mro__)


# from abc import ABCMeta
#
# print(ABCMeta.__class__)
# print(ABCMeta.__mro__)


class OurMetaClass(type):

    def __new__(cls, *args):
        print('Our meta class!')
        return super(OurMetaClass, cls).__new__(cls, *args)


class Study(object, metaclass=OurMetaClass):

    item = 'English'

    def score(self):
        return 100


print(OurMetaClass.__class__)
print(OurMetaClass.__mro__)
s = Study()
print(s.item)
print(s.score())
print(s)
print(s.__class__)
print(Study.__class__)

