# coding=utf-8

# import time
#
#
# def coroutine1():
#     for i in range(5):
#         print("-----coroutine1-----")
#         yield
#         time.sleep(1)
#
#
# def coroutine2():
#     for i in range(5):
#         print("-----coroutine2-----")
#         yield
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     c1 = coroutine1()
#     c2 = coroutine2()
#     for i in range(3):
#         next(c1)
#         next(c2)


# import greenlet
# import time
#
#
# def greenlet1():
#     for i in range(3):
#         print("-----greenlet1-----")
#         time.sleep(1)
#         g2.switch()
#
#
# def greenlet2():
#     for i in range(3):
#         print("-----greenlet2-----")
#         time.sleep(1)
#         g1.switch()
#
#
# g1 = greenlet.greenlet(greenlet1)
# g2 = greenlet.greenlet(greenlet2)
#
# # 切换到gr1中运行
# g1.switch()


# import gevent
# import time
#
#
# def gevent_func():
#     for i in range(3):
#         print(gevent.getcurrent(), i)
#         gevent.sleep(1)
#
#
# start = time.time()
# gevent_func()
# gevent_func()
# gevent_func()
# end = time.time()
# print('One coroutine: ', end - start)
#
# gevent_start = time.time()
# g1 = gevent.spawn(gevent_func,)
# g2 = gevent.spawn(gevent_func,)
# g3 = gevent.spawn(gevent_func, )
# g1.join()
# g2.join()
# g3.join()
# gevent_end = time.time()
# print('Multi coroutine: ', gevent_end - gevent_start)


import gevent
from gevent import monkey
import time


monkey.patch_all()


def gevent_func():
    for i in range(3):
        print(gevent.getcurrent(), i)
        time.sleep(1)


gevent_start = time.time()
g1 = gevent.spawn(gevent_func,)
g2 = gevent.spawn(gevent_func,)
g3 = gevent.spawn(gevent_func, )
g1.join()
g2.join()
g3.join()
gevent_end = time.time()
print('Multi coroutine: ', gevent_end - gevent_start)
