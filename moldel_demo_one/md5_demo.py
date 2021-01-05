# coding=utf-8
# import hashlib
#
#
# md = hashlib.md5()
# md.update('abcdef'.encode('utf-8'))
# print(md.hexdigest())


# import hashlib
#
#
# md = hashlib.md5('abcdefg'.encode('utf-8'))
# # print(dir(md))
# print(md.hexdigest())
# print(md.block_size)
# print(md.name)
# x = md.copy()
# print(x.hexdigest())
# print(x.name)
# print("-" * 50)
# print(md.digest())
# print(md.digest_size)


import hashlib
import binascii

md = hashlib.md5('abcdefg'.encode('utf-8'))
print(md.hexdigest())
print(md.digest())
print("-" * 50)
print(binascii.hexlify(md.digest()).decode('utf-8'))
print(binascii.unhexlify(md.hexdigest()))
