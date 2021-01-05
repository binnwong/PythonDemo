# coding=utf-8
import calendar
#
# print(calendar.calendar(3019, w=4, l=1, c=6, m=4))
#
# calendar.setfirstweekday(6)
# print(calendar.firstweekday())
# print(calendar.calendar(3019, w=4, l=1, c=6, m=4))
# calendar.prcal(2019, w=2, l=1, c=6)


import calendar


print("month: \n", calendar.month(2019, 10, w=0, l=0))
# calendar.prmonth(2019, 10, w=0, l=0)
print("monthcalendar: ", calendar.monthcalendar(2019, 11))
# 返回两个数，这个月的第一天是星期几，这个月有多少天
print("monthrange: ", calendar.monthrange(2019, 10))


import calendar

tupletime = (2020, 10, 1, 8, 30, 30)
print(calendar.timegm(tupletime))
print(calendar.weekday(2019, 12, 1))
print(calendar.isleap(2020))
print(calendar.leapdays(2019, 2021))
