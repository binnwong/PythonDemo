# coding=utf-8


def say_hello():
    print("hello world!")


# say_hello()


def say_sorry(n):
    for _ in range(n):
        print("I'm sorry!")


# say_sorry(10000)


def cycle(n):
    for i in range(1, n):
        for j in range(1, n):
            print("i={}".format(i), end=" ")
            print("j={}".format(j), end=" ")
            print("i*j={}".format(i*j))


# cycle(10)


def branch(n):
    if n % 2 == 0:
        for i in range(0, n, 2):
            print(i/2)
    else:
        print(n)


# branch(12)


def search(n, m):
    data_list = range(1, n)
    for i in data_list:
        if i == m:
            return i
    else:
        return -1


print(search(10, 1))
