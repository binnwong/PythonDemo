# coding=utf-8
# import hashlib
#
#
# sh = hashlib.sha1()
# sh.update('abcdef'.encode('utf-8'))
# print('sha1:\t', sh.hexdigest())
#
# sh = hashlib.sha224()
# sh.update('abcdef'.encode('utf-8'))
# print('sha224:\t', sh.hexdigest())
#
# sh = hashlib.sha256()
# sh.update('abcdef'.encode('utf-8'))
# print('sha256:\t', sh.hexdigest())
#
# sh = hashlib.sha384()
# sh.update('abcdef'.encode('utf-8'))
# print('sha384:\t', sh.hexdigest())
#
# sh = hashlib.sha512()
# sh.update('abcdef'.encode('utf-8'))
# print('sha512:\t', sh.hexdigest())
#
# sh = hashlib.sha3_224()
# sh.update('abcdef'.encode('utf-8'))
# print('sha3_224:', sh.hexdigest())
#
# sh = hashlib.sha3_256()
# sh.update('abcdef'.encode('utf-8'))
# print('sha3_256:', sh.hexdigest())
#
# sh = hashlib.sha3_384()
# sh.update('abcdef'.encode('utf-8'))
# print('sha3_384:', sh.hexdigest())
#
# sh = hashlib.sha3_512()
# sh.update('abcdef'.encode('utf-8'))
# print('sha3_512:', sh.hexdigest())


# import hashlib
#
#
# sh = hashlib.blake2b()
# sh.update('abcdef'.encode('utf-8'))
# print(sh.hexdigest())
#
# sh = hashlib.blake2s()
# sh.update('abcdef'.encode('utf-8'))
# print(sh.hexdigest())
#
# sh = hashlib.shake_128()
# sh.update('abcdef'.encode('utf-8'))
# print(sh.hexdigest(100))
# print(sh.digest(10))
#
# sh = hashlib.shake_256()
# sh.update('abcdef'.encode('utf-8'))
# print(sh.hexdigest(100))
# print(sh.digest(10))


import hashlib
import binascii


sh = hashlib.shake_256()
sh.update('abcdef'.encode('utf-8'))
print(sh.hexdigest(10))
print(sh.digest(10))
print("-" * 50)
print(binascii.hexlify(sh.digest(10)).decode('utf-8'))
print(binascii.unhexlify(sh.hexdigest(10)))
