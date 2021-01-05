# coding=utf-8
import base64
import string
import random


# str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
# print(str[31])
# print(str[50])
# print(str[0])
# print(str[16])

# base_str = string.ascii_letters + string.punctuation
# print(base_str)
# result_str = ''.join(random.choices(base_str, k=20))
# print(result_str)
# result = base64.encodebytes(bytes(result_str.encode('utf-8'))).decode('utf-8')
# print(result)
# result_back = base64.decodebytes(bytes(result.encode('utf-8'))).decode('utf-8')
# print(result_back)

# python2
# result_str = 'UVWXYZ!#$%&()*+,-./'
# print(result_str)
# result = base64.encodestring(bytes(result_str.encode('utf-8'))).decode('utf-8')
# print(result)
# result_back = base64.decodestring(bytes(result.encode('utf-8'))).decode('utf-8')
# print(result_back)

# base_str = string.ascii_letters + string.punctuation
# print(base_str)
# result_str = ''.join(random.choices(base_str, k=20))
# print(result_str)
# with open('base64.txt', 'wb') as f:
#     f.write(bytes(result_str.encode('utf-8')))
# base64.encode(open('base64.txt', 'rb'), open('base64.b64', 'wb'))
# print(open("base64.b64").read())
#
# base64.decode(open('base64.b64', 'rb'), open('base64.new', 'wb'))
# print(open("base64.new").read())

# base_str = string.ascii_letters + string.punctuation
# print(base_str)
# result_str = ''.join(random.choices(base_str, k=20))
# print(result_str)
# result = base64.b64encode(bytes(result_str.encode('utf-8'))).decode('utf-8')
# print(result)
# result_back = base64.b64decode(bytes(result.encode('utf-8'))).decode('utf-8')
# print(result_back)
