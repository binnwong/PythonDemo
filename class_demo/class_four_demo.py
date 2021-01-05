# coding=utf-8


# class House(object):
#
#     price = 'high'
#
#
# print(House.price)
# h = House()
# print(h.price)
#
# House.price = 'too high'
# print(House.price)
# print(h.price)
#
# print('-' * 20)
# h.price = 'high'
# print(House.price)
# print(h.price)


# class House(object):
#
#     __price = 'high'
#
#     @classmethod
#     def get_price(cls):
#         return cls.__price
#
#
# print(House.get_price())
#
# h = House()
# print(h.get_price())


class House(object):

    __price = 'high'

    @classmethod
    def get_price(cls):
        return cls.__price

    @staticmethod
    def description():
        return 'No money, no house'


print(House.description())

h = House()
print(h.description())
