from callback_B import trade_meeting


def trade_cn_us():
    """大大赴美,中美贸易磋商"""
    print()
    print("---++  准备行程,大大赴美  ++---")
    trade_meeting(ready_info)
    print("---++  会谈结束,带喜讯回国  ++---")


def ready_info():
    """准备商谈内容"""
    print()
    print("---++  会议中提出要求  ++---")
    print()


if __name__ == '__main__':
    trade_cn_us()


"""
0. 运行代码
1. 模块1 函数A 执行一段代码
2. 模块1 函数A 调用 模块2中的函数B
3. 模块2 函数B 执行一段代码
4. 模块2 函数B 调用 模块1中的函数C
5. 模块1 函数C 执行 完成
6. 模块2 函数B 执行剩余代码
7. 模块1 函数A 执行剩余代码
8. 终止
"""
