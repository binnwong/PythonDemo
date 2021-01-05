# coding=utf-8


class Women(object):

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def shop(self):
        print("Go Shopping!")

    def photo(self):
        print('Photo self!')


wo = Women('kitty', 18, 1.57)
# print(dir(wo))

# print(getattr(wo, 'name'))
# # print(getattr(wo, 'friend'))
# print(getattr(wo, 'friend', 'me'))
# shop = getattr(wo, 'shop')
# shop()

# setattr(wo, 'height', 1.66)
# print(getattr(wo, 'height'))
# setattr(wo, 'home', 'sz')
# print(getattr(wo, 'home'))

# print(hasattr(wo, 'name'))
# print(hasattr(wo, 'shop'))
# print(hasattr(wo, 'job'))

print(vars(wo))
