# coding=utf-8
import multiprocessing


a = multiprocessing.Value('i', 0)


def test_func(num, q):
    global a
    for i in range(num):
        a.value += 1
    print(a.value)


# test_func(5)
#
# print(a)
# print(globals())


if __name__ == '__main__':
    # print(a.value)
    q = multiprocessing.Manager().Queue()
    po = multiprocessing.Pool(4)
    for j in range(10):
        po.apply_async(test_func, (j, q))
    po.close()
    po.join()

    print(a.value)

    # d = multiprocessing.Manager().list(range(5))
    # print(d)
    # print(type(d))
    # for c in d:
    #     print(c)

    # p = multiprocessing.Process(target=test_func, args=(d.value,))
    # p.start()
    # p.join()
    # print(a)
