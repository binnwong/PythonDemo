# try:
#     print(arg)
# except:
#     print("参数未定义!")


# try:
#     arg = 'Python 碎片'
#     print(arg)
# except:
#     print("参数为定义!")
# else:
#     print("代码质量很高,没有异常!")


# try:
#     num_str = "10.0"
#     num = int(num_str)
#     print(num)
# except ValueError as e:
#     print(e)
# else:
#     print("代码质量很高,没有异常!")
# finally:
#     print("最终执行的代码")


# try:
#     try:
#         num_str = "10.0"
#         num = int(num_str)
#         print(num)
#     except (NameError, SyntaxError) as e:
#         print(e)
#     finally:
#         print('代码结束')
# except Exception as e:
#     print("天网恢恢:{}".format(e))


class MoneyException(Exception):
    '''自定义的异常类'''

    def __init__(self, money):
        self.money = int(money)

    def __str__(self):
        if self.money > 0:
            return "Good!"
        else:
            return "Gun!"


try:
    money = -100
    if money > 0:
        exc = MoneyException(money)
        print(exc)
    else:
        raise MoneyException(money)
except MoneyException as e:
    print("自己留着吧!", e)
