# coding=utf-8
# import re
#
#
# test_str = 'When面对困难111, we 正面面对, yes, 加油！666'
# comp = re.match(r'\w+', test_str)
# print(comp.group())


# coding=utf-8
# import re
#
#
# test_str = 'When面对困难111, we 正面面对, yes, 加油！666'
# comp = re.compile(r'[\u4E00-\u9FA5]+')
# re_result = comp.findall(test_str)
# print(re_result)


# coding=utf-8
# import re
#
#
# test_str = u'When面对困难111, we 正面面对, yes, 加油！666'
# comp = re.compile(u'[\u4E00-\u9FA5]+')
# re_result = comp.findall(test_str)
# print(re_result)
# for s in re_result:
#     s = s.encode('gbk')
#     print(s)


# coding=utf-8
import re


test_str = 'When面对困难111, we 正面面对, yes, 加油！666'
comp = re.compile(u'[\u4E00-\u9FA5]+')
# test_str = unicode(test_str, encoding='utf-8')
# re_result = comp.findall(test_str)
re_result = comp.findall(test_str.decode('utf-8'))
print(re_result)
for s in re_result:
    s = s.encode('gbk')
    print(s)


# coding=utf-8
# import re
# import sys
#
#
# test_str = 'When面对困难111, we 正面面对, yes, 加油！666'
# if sys.version[0] == '3':
#     comp = re.compile(r'[\u4E00-\u9FA5]+')
#     re_result = comp.findall(test_str)
# else:
#     comp = re.compile(u"[\u4E00-\u9FA5]+")
#     re_result = comp.findall(test_str.decode('utf-8'))
#     re_result = [s.encode('gbk') for s in re_result]
# print(re_result)
# for a in re_result:
#     print(a)


# coding=utf-8
import re
import sys
import json


test_str = 'When面对困难111, we 正面面对, yes, 加油！666'
if sys.version[0] == '3':
    comp = re.compile(r'[\u4E00-\u9FA5]+')
    re_result = comp.findall(test_str)
else:
    comp = re.compile(u"[\u4E00-\u9FA5]+")
    re_result = comp.findall(test_str.decode('utf-8'))
    re_result = [s.encode('gbk') for s in re_result]
    # re_result = repr(re_result).decode('string-escape')  # 方法一
    re_result = json.dumps(re_result, ensure_ascii=False)  # 方法二
print(re_result)
print(type(re_result))
