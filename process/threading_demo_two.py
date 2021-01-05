# coding=utf-8

# from threading import Thread
#
#
# list_a = [1, 2, 3]
#
#
# def add_list():
#     global list_a
#     list_a.append(100)
#     print(list_a)
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=add_list)
#     t2 = Thread(target=add_list)
#     print(t1.name)
#     t1.start()
#     print(t2.name)
#     t2.start()


# from threading import Thread
#
#
# num = 0
#
#
# def add_num():
#     global num
#     for i in range(100000):
#         num += 1
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=add_num)
#     t2 = Thread(target=add_num)
#     t3 = Thread(target=add_num)
#     t1.start()
#     t2.start()
#     t3.start()
#     print(num)


# from threading import Thread, Lock, enumerate
# import time
#
#
# num = 0
# mutex = Lock()
#
#
# def add_num():
#     global num
#     for i in range(1000000):
#         mutex.acquire()
#         num += 1
#         mutex.release()
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=add_num)
#     t2 = Thread(target=add_num)
#     t3 = Thread(target=add_num)
#     t1.start()
#     t2.start()
#     t3.start()
#
#     while len(enumerate()) != 1:
#         time.sleep(1)
#     print(num)


from threading import Thread, Lock
import time

mutex_x = Lock()
mutex_y = Lock()


def x_func():
    print('X...')
    mutex_x.acquire()
    print('Lock x something')
    time.sleep(1)

    result = mutex_y.acquire(timeout=10)
    print(result)
    print('Use y something')
    time.sleep(1)
    # if result:
    #     mutex_y.release()
    print(result)
    print('x...')
    mutex_x.release()


def y_func():
    print('Y...')
    mutex_y.acquire()
    print('Lock y something')
    time.sleep(1)
    mutex_x.acquire()
    print('Use x something')
    time.sleep(1)
    mutex_x.release()
    print('y...')
    mutex_y.release()


if __name__ == '__main__':
    t1 = Thread(target=x_func)
    t2 = Thread(target=y_func)

    t1.start()
    t2.start()
