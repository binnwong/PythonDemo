# coding=utf-8
# class Electrical(object):
#
#     def __init__(self, name):
#         self.name = name
#         print('Electrical init')
#
#
# class Phone(Electrical):
#
#     def __init__(self, name, price):
#         Electrical.__init__(self, name)
#         self.price = price
#         print('Phone init')
#
#
# class Computer(Electrical):
#
#     def __init__(self, name, config):
#         Electrical.__init__(self, name)
#         self.config = config
#         print('Computer init')
#
#
# class HuaWei(Phone, Computer):
#
#     def __init__(self, name, price, config):
#         Phone.__init__(self, name, price)
#         Computer.__init__(self, name, config)
#         print('HuaWei init')
#
#
# h = HuaWei('huawei', 100, 'i7')


# class Electrical(object):
#
#     def __init__(self, name):
#         self.name = name
#         print('Electrical init')
#
#
# class Phone(Electrical):
#
#     def __init__(self, price, *args):
#         super(Phone, self).__init__(*args)
#         self.price = price
#         print('Phone init')
#
#
# class Computer(Electrical):
#
#     def __init__(self, config, *args):
#         super(Computer, self).__init__(*args)
#         self.config = config
#         print('Computer init')
#
#
# class HuaWei(Phone, Computer):
#
#     def __init__(self, name, price, config):
#         super(HuaWei, self).__init__(name, price, config)
#         print('HuaWei init')
#
#
# h = HuaWei('huawei', 100, 'i7')


class Electrical(object):

    def chat(self):
        print('Chat with friend in electrical!')

    def watch_movie(self):
        print('Watch movie in electrical!')

    def game(self):
        print('Play game in electrical!')


class Phone(Electrical):

    def game(self):
        print('Play game in phone!')


class Computer(Electrical):

    def watch_movie(self):
        print('Watch movie in computer!')

    def game(self):
        print('Play game in computer!')


class HuaWei(Phone, Computer):
    pass


h = HuaWei()
h.game()
h.watch_movie()
h.chat()

print(HuaWei.__mro__)


# class Electrical(object):
#
#     def __init__(self, name):
#         self.name = name
#         print('Electrical init')
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
# class Phone(Electrical):
#
#     def __init__(self, price, *args):
#         super(Phone, self).__init__(*args)
#         self.price = price
#         print('Phone init')
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
#
#
# class Computer(Electrical):
#
#     def __init__(self, config, *args):
#         super(Computer, self).__init__(*args)
#         self.config = config
#         print('Computer init')
#
#     def game(self):
#         print('Play game in computer!')
#
#     def coding(self):
#         print('Coding something!')
#
#
# class HuaWei(Phone, Computer):
#
#     def __init__(self, name, price, config):
#         super(HuaWei, self).__init__(name, price, config)
#         print('HuaWei init')
#
#
# h = HuaWei('huawei', 100, 'i7')
