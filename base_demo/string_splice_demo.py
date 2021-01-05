# coding=utf-8
# str_a = 'python'
# print('hello', str_a, '!')

# str_b = 'It is summer ' 'of 2019!'
# print(str_b)


# str_c = 'Love makes ' \
#         'man grow up ' \
#         'or sink down!'
# print(str_c)

# str_d = 'string'
# str_e = 'demo'
# print(str_d + str_e)
# str_e += str_d
# print(str_e)


# str_f = 'a-' * 10
# print(str_f)


# str_g = 'aaaaaaaaaaaa%saaaaaaaaa' % 'A'
# print(str_g)
# str_h = 'aaaaaaaaaaaa%06daaaaaaaaa' % 10
# print(str_h)
# str_i = 'aaaaaaaaaaaa%.03faaaaaaaaa' % 0.77
# print(str_i)


# str_j = 'python {}! format {}!'.format(666, 999)
# print(str_j)
# str_k = '生如夏花之{a}，死如秋叶之{b}！'.format(b='静美', a='绚烂')
# print(str_k)


# list_l = ['生', '如', '夏', '花', '之', '绚', '烂', '，', '死', '如', '秋', '叶', '之', '静', '美', '！']
# str_l = ''.join(list_l)
# print(str_l)
# tuple_m = ('生', '如', '夏', '花', '之', '绚', '烂', '，', '死', '如', '秋', '叶', '之', '静', '美', '！')
# str_m = '-'.join(tuple_m)
# print(str_m)


# from string import Template
#
#
# t = Template('${s1} ${s2}!')
#
# str_n = t.safe_substitute(s1='Hello', s2='Python')
# str_s = t.substitute(s1='Hello', s2={'a':1, 'b': 2, 'c': 320})
# print(t)
# print(str_n)
# print(str_s)


# o = 6666666666
# p = 7777777777
# str_o = f'Python {o} hello {p} !'
# print(str_o)


def add_string(str):
    return str.upper()


str = 'a k q j 10'
str_p = f'顺子! {add_string(str)}'
print(str_p)

