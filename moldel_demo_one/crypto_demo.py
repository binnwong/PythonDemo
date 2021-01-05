# coding=utf-8
# from Crypto import Random
# from Crypto.PublicKey import RSA
#
#
# random_generator = Random.new().read
# print(random_generator)
# rsa = RSA.generate(2048, random_generator)
# # 生成私钥
# private_key = rsa.exportKey()
# print(private_key.decode('utf-8'))
# print("-" * 30 + "分割线" + "-" * 30)
# # 生成公钥
# public_key = rsa.publickey().exportKey()
# print(public_key.decode('utf-8'))


from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import base64


random_generator = Random.new().read
rsa = RSA.generate(2048, random_generator)

private_key = rsa.exportKey()
with open("private_a.rsa", 'wb') as f:
    f.write(private_key)

public_key = rsa.publickey().exportKey()
with open("public_a.rsa", 'wb') as f:
    f.write(public_key)

# 使用公钥对内容进行rsa加密
message = "需要加密的信息"
with open('public_a.rsa') as f:
    key = f.read()
    pub_key = RSA.importKey(str(key))
    cipher = PKCS1_cipher.new(pub_key)
    rsa_text = base64.b64encode(cipher.encrypt(bytes(message.encode("utf8"))))
    print(rsa_text.decode('utf-8'))

# 使用私钥对内容进行rsa解密
with open('private_a.rsa') as f:
    key = f.read()
    pri_key = RSA.importKey(key)
    cipher = PKCS1_cipher.new(pri_key)
    back_text = cipher.decrypt(base64.b64decode(rsa_text), 0)
    print(back_text.decode('utf-8'))


# from Crypto.PublicKey import RSA
# from Crypto.Hash import SHA
# import base64
# from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
#
#
# message = "需要加密的信息"
# # 使用私钥生成签名
# with open('private_a.rsa') as f:
#     key = f.read()
#     pri_key = RSA.importKey(key)
#     signer = PKCS1_signature.new(pri_key)
#     digest = SHA.new()
#     digest.update(message.encode("utf8"))
#     sign = signer.sign(digest)
#     signature = base64.b64encode(sign)
#     print(signature.decode('utf-8'))
#
# # 使用公钥验证签名
# with open('public_a.rsa') as f:
#     key = f.read()
#     pub_key = RSA.importKey(key)
#     verifier = PKCS1_signature.new(pub_key)
#     digest = SHA.new()
#     digest.update(message.encode("utf8"))
#     print(verifier.verify(digest, base64.b64decode(signature)))


# from Crypto.Cipher import AES
# from binascii import b2a_hex, a2b_hex
#
#
# message = "需要加密的信息"
# key = 'aes_keysaes_keysaes_keys'
# mode = AES.MODE_OFB
# cryptor = AES.new(key.encode('utf-8'), mode, b'0000000000000000')
# length = 16
# count = len(message)
# if count % length != 0:
#     add = length - (count % length)
# else:
#     add = 0
# message = message + ('\0' * add)
# ciphertext = cryptor.encrypt(message.encode('utf-8'))
# result = b2a_hex(ciphertext)
# print(result.decode('utf-8'))
#
# cryptor = AES.new(key.encode('utf-8'), mode, b'0000000000000000')
# plain_text = cryptor.decrypt(a2b_hex(result))
# print(plain_text.decode('utf-8').rstrip('\0'))

