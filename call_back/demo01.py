"""回调函数"""


def watch_s8():
    """用户观看s8"""
    print()
    print("---++  用户打开斗鱼  ++---")
    douyu_live()
    print("---++  用户观看直播  ++---")


def douyu_live():
    """斗鱼直播s8"""
    print()
    print("---++  斗鱼获取资源  ++---")
    user_click()
    print("---++  斗鱼播放视频  ++---")
    print()


def user_click():
    """用户点击播放"""
    print()
    print("---++  用户点击进入  ++---")
    print()


if __name__ == '__main__':
    watch_s8()
