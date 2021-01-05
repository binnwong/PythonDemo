class China(object):
    """国内事项"""

    def trade_cn_us(self):
        """大大赴美,中美贸易磋商"""
        print()
        print("---++  准备行程,大大赴美  ++---")
        us = American()
        us.trade_meeting(self.ready_info)
        print("---++  会谈结束,带喜讯回国  ++---")

    def ready_info(self):
        """准备商谈内容"""
        print()
        print("---++  会议中提出要求  ++---")
        print()


class American(object):
    """美国事项"""

    def trade_meeting(self, callback_func):
        """贸易会谈并签署协议"""
        print()
        print("---++  与特朗普开始会谈  ++---")
        callback_func()
        print("---++  会谈结束签署协议  ++---")
        print()


if __name__ == '__main__':
    cn = China()
    cn.trade_cn_us()
