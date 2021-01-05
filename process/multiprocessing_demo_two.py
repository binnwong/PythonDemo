# coding=utf-8
# from multiprocessing import Process, Queue
# import time
#
#
# def put_card(queue):
#     """往队列中添加数据"""
#     for card in ['A', 'K', 'Q', 'J', '10']:
#         print('Put {} to queue...'.format(card))
#         queue.put(card)
#         time.sleep(1)
#
#
# def get_card(queue):
#     """从队列中取出数据"""
#     while True:
#         if not queue.empty():
#             card = queue.get(True)
#             print('Get {} from queue.'.format(card))
#             time.sleep(1)
#         else:
#             break
#
#
# if __name__ == "__main__":
#     q = Queue()
#     pp = Process(target=put_card, args=(q,))
#     pg = Process(target=get_card, args=(q,))
#     pp.start()
#
#     pg.start()
#     pg.join()
#     print(pg.is_alive())


from multiprocessing import Pool
import os
import time


def task(num):
    print("Sub process {} start, process id is {}".format(num, os.getpid()))
    time.sleep(1)
    print("Sub process {} end".format(num))


if __name__ == '__main__':

    po = Pool(3)
    for i in range(10):
        po.apply_async(task, (i + 1,))

    # time.sleep(2)
    # po.terminate()
    po.close()
    po.join()


# from multiprocessing import Pool, Manager
# import time
#
#
# def put_card(queue):
#     """往队列中添加数据"""
#     for card in ['A', 'K', 'Q', 'J', '10']:
#         print('Put {} to queue...'.format(card))
#         queue.put(card)
#         time.sleep(1)
#
#
# def get_card(queue):
#     """从队列中取出数据"""
#     while True:
#         if not queue.empty():
#             card = queue.get(True)
#             print('Get {} from queue.'.format(card))
#             time.sleep(1)
#         else:
#             break
#
#
# if __name__ == "__main__":
#     # q = Queue() 程序会直接终止
#     q = Manager().Queue()
#     p = Pool()
#     p.apply_async(put_card, args=(q,))
#     p.apply_async(get_card, args=(q,))
#
#     p.close()
#     p.join()
