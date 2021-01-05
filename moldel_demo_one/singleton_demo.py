# coding=utf-8


# def singleton_func(cls):
#     instances = {}
#
#     def _singleton(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return _singleton
#
#
# @singleton_func
# class Phone(object):
#
#     def phone_id(self):
#         return id(self)
#
#
# p1 = Phone()
# p2 = Phone()
# print(p1.phone_id())
# print(p2.phone_id())


# class SingletonInstance(object):
#
#     def __call__(self, *args, **kwargs):
#         return self
#
#
# SingletonInstance = SingletonInstance()
# s1 = SingletonInstance()
# s2 = SingletonInstance()
# print(id(s1))
# print(id(s2))


# class SingletonDecorator(object):
#     _instance = None
#
#     def __init__(self, cls):
#         self._cls = cls
#
#     def __call__(self, *args, **kwargs):
#         if self._instance is None:
#             self._instance = self._cls(*args, **kwargs)
#         return self._instance
#
#
# @SingletonDecorator
# class Phone(object):
#
#     def phone_id(self):
#         return id(self)
#
#
# p1 = Phone()
# p2 = Phone()
# print(p1.phone_id())
# print(p2.phone_id())


# class SingletonClass(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(SingletonClass, cls).__new__(cls)
#         return cls._instance
#
#     _is_init = False
#
#     def __init__(self):
#         if self._is_init is False:
#             print('-*-')
#             self._is_init = True
#
#
# s1 = SingletonClass()
# s2 = SingletonClass()
# print(id(s1))
# print(id(s2))


class SingletonMeta(type, object):

    # def __init__(self, *args, **kwargs):
    #     self._instance = None
    #     super(SingletonMeta, self).__init__(*args, **kwargs)

    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super(SingletonMeta, self).__call__(*args, **kwargs)
        return self._instance


class Phone(object, metaclass=SingletonMeta):

    def phone_id(self):
        return id(self)


p1 = Phone()
p2 = Phone()
print(p1.phone_id())
print(p2.phone_id())
