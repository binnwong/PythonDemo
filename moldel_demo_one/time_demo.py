# coding=utf-8
# import time


# print(time.time())
# print(time.localtime())
# print(time.localtime(time.time()))

# # 时间戳转换成时间字符串
# time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# print(time_str)
#
# print(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))
# # 时间字符串转换成时间戳
# time_stamp = time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))
# print(time_stamp)


from datetime import datetime


print(datetime.now())
print(datetime.now().timetuple())

# datetime对象转换成时间字符串
datetime_str = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
print(datetime_str)

# datetime对象转换成时间戳
datetime_stamp = datetime.timestamp(datetime.now())
print(datetime_stamp)

# 时间字符串转datetime对象，再转时间戳
datetime_stamp2 = datetime.timestamp(datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S'))
print(datetime_stamp2)

# 时间戳转datetime对象，再转时间字符串
datetime_str2 = datetime.strftime(datetime.fromtimestamp(datetime_stamp2), '%Y-%m-%d %H:%M:%S')
print(datetime_str2)
