# coding=utf-8
def insert_time_test():
    insert_list = list()
    for i in range(10):
        insert_list.insert(0, i)


def append_time_test():
    append_list = list()
    for i in range(10):
        append_list.append(i)


if __name__ == '__main__':
    import timeit
    # insert_time_timeit = timeit.timeit(stmt='insert_time_test()',
    #                                    setup='from __main__ import insert_time_test')
    # print('insert_time_timeit: ', insert_time_timeit)
    # append_time_timeit = timeit.timeit(stmt='append_time_test()',
    #                                    setup='from __main__ import append_time_test')
    # print('append_time_timeit: ', append_time_timeit)

    # insert_time_timeit = timeit.timeit(stmt='list(insert_list.insert(0, i) for i in init_list)',
    #                                    setup='insert_list=list();init_list=range(10)',
    #                                    number=100000)
    # print('insert_time_timeit: ', insert_time_timeit)
    # append_time_timeit = timeit.timeit(stmt='list(append_list.append(i) for i in init_list)',
    #                                    setup='append_list=list();init_list=range(10)',
    #                                    number=100000)
    # print('append_time_timeit: ', append_time_timeit)

    # insert_time_repeat = timeit.repeat(stmt='insert_time_test()',
    #                                    setup='from __main__ import insert_time_test')
    # print('insert_time_repeat: ', insert_time_repeat)
    # append_time_repeat = timeit.repeat(stmt='append_time_test()',
    #                                    setup='from __main__ import append_time_test')
    # print('append_time_repeat: ', append_time_repeat)

    # insert_time_repeat = timeit.repeat(stmt='list(insert_list.insert(0, i) for i in init_list)',
    #                                    setup='insert_list=list();init_list=range(10)',
    #                                    repeat=5,
    #                                    number=10000)
    # print('insert_time_repeat: ', insert_time_repeat)
    # append_time_repeat = timeit.repeat(stmt='list(append_list.append(i) for i in init_list)',
    #                                    setup='append_list=list();init_list=range(10)',
    #                                    repeat=5,
    #                                    number=10000)
    # print('append_time_repeat: ', append_time_repeat)

    # timer_insert = timeit.Timer(stmt='insert_time_test()', setup='from __main__ import insert_time_test')
    # insert_time_timeit = timer_insert.timeit(number=1000000)
    # print('insert_time_timeit: ', insert_time_timeit)
    # insert_time_repeat = timer_insert.repeat(number=1000000)
    # print('insert_time_repeat: ', insert_time_repeat)

    timer_append = timeit.Timer(stmt='append_time_test()', setup='from __main__ import append_time_test')
    append_time_timeit = timer_append.timeit(number=1000000)
    print('append_time_timeit: ', append_time_timeit)
    append_time_repeat = timer_append.repeat(number=1000000)
    print('append_time_repeat: ', append_time_repeat)
