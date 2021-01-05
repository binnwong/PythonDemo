# coding=utf-8
# from threading import Thread, enumerate
# import time
#
#
# def play_game():
#     for i in range(5):
#         print('Playing game!', end=' | ')
#         time.sleep(1)
#
#
# def listen_song():
#     for i in range(5):
#         print('Listening song!', end=' | ')
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     play_game()
#     listen_song()
#     end = time.time()
#     print('\n', enumerate())
#     print('One thread cost time: ', end - start)
#
#     multi_start = time.time()
#     t1 = Thread(target=play_game)
#     t2 = Thread(target=listen_song)
#     t1.start()
#     t2.start()
#     print('\n', enumerate())
#     while len(enumerate()) != 1:
#         time.sleep(1)
#     multi_end = time.time()
#     print('\nMulti thread cost time: ', multi_end - multi_start)


# from threading import Thread, enumerate
# import time
#
#
# # 自定义类，继承Thread
# class OurThread(Thread):
#     def run(self):
#         for i in range(3):
#             print("Play game " + self.name, end=' | ')
#             time.sleep(1)
#
#
# if __name__ == '__main__':
#     # 通过MyThread创建线程对象
#     o1 = OurThread()
#     o2 = OurThread()
#     print(enumerate())
#     o1.start()
#     o2.start()
#     print('\n', enumerate())


from threading import Thread
import time


class OurThread(Thread):
    def run(self):
        for i in range(3):
            print("Play game {} ".format(i) + self.name)
            time.sleep(1)


if __name__ == '__main__':
    for i in range(3):
        o = OurThread()
        o.start()
