# coding=utf-8
# list_a = [a ** 2 for a in range(6)]
# # Python中没有元组推导式，这行代码会得到一个生成器
# genera_a = (a ** 2 for a in range(6))
# print(list_a)
# print(genera_a)
# print(next(genera_a), end=' ')
# print(next(genera_a), end=' ')
# print(next(genera_a), end=' ')
# print(next(genera_a), end=' ')
# print(next(genera_a), end=' ')
# print(next(genera_a), end=' ')
# print(next(genera_a), end=' ')


# def feibo_func(n):
#     current_index = 0
#     num1, num2 = 0, 1
#     while current_index < n:
#         """
#          1. 假如函数中有yield，则不再是函数，而是生成器
#          2. yield 会产生一个断点,返回数据后暂时阻塞在此
#          3. 假如yield后面紧接着一个数据，就会把数据返回，
#             作为next()函数或者for ...in...迭代出的下一个值
#         """
#         yield num1
#         num1, num2 = num2, num1 + num2
#         current_index += 1
#
#
# gen = feibo_func(10)
# print(gen)
#
# for num in gen:
#     print(num, end=' ')


def genera_func():
    for i in range(6):
        arg = yield i
        print(arg)


print(genera_func())
gen = genera_func()
print(next(gen))
print(gen.send('aaaaa'))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
