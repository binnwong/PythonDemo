# coding=utf-8
class SequenceQueue(object):

    def __init__(self):
        self.__members = list()

    def is_empty(self):
        return not len(self.__members)

    def show(self):
        if self.is_empty():
            print('队列为空')
            return
        for member in self.__members:
            print('|' + member, end='')
        print()

    def enter(self, data):
        self.__members.insert(0, data)

    def outer(self):
        if self.is_empty():
            return
        return self.__members.pop()

    def length(self):
        return len(self.__members)

    def check(self, index):
        if index < 0 or index > len(self.__members)-1:
            raise IndexError
        return self.__members[index]


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkQueue(object):

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return not self.__head

    def show(self):
        if self.is_empty():
            print('队列为空')
            return
        cur = self.__head
        while cur is not None:
            if cur.next is not None:
                print('|' + cur.data, end='')
            else:
                print('|' + cur.data)
            cur = cur.next

    def enter(self, data):
        node = Node(data)
        node.next = self.__head
        self.__head = node

    def outer(self):
        if self.is_empty():
            return
        cur = self.__head
        prev = None
        while cur.next is not None:
            prev = cur
            cur = cur.next
        if cur == self.__head:
            self.__head = self.__head.next
            return
        prev.next = cur.next
        return cur.data

    def length(self):
        length = 0
        cur = self.__head
        while cur is not None:
            length += 1
            cur = cur.next
        return length

    def check(self, index):
        if index < 0 or index >= self.length():
            raise IndexError
        cur = self.__head
        for _ in range(index):
            cur = cur.next
        return cur.data


if __name__ == '__main__':
    sq = SequenceQueue()
    print("is_empty: ", sq.is_empty())
    sq.show()

    sq.enter('u')
    sq.enter('v')
    sq.enter('x')
    sq.enter('y')
    sq.enter('z')
    sq.show()
    print(sq.outer())
    sq.show()

    print("sequence queue length: ", sq.length())
    print("index member is: ", sq.check(2))

    lq = LinkQueue()
    print("is_empty: ", lq.is_empty())
    lq.show()

    lq.enter('U')
    lq.enter('V')
    lq.enter('X')
    lq.enter('Y')
    lq.enter('Z')
    lq.show()
    print(lq.outer())
    lq.show()

    print("link queue length: ", lq.length())
    print("index member is: ", lq.check(2))
