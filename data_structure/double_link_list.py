# coding=utf-8
class Node(object):

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkList(object):

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return not self.__head

    def show(self):
        if self.is_empty():
            print('空链表')
            return
        cur = self.__head
        while cur is not None:
            if cur.next is not None:
                print(cur.data, end='←→')
            else:
                print(cur.data)
            cur = cur.next

    def add(self, data):
        node = Node(data)
        if self.is_empty():
            self.__head = node
            return
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def append(self, data):
        if self.is_empty():
            self.add(data)
            return
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        node = Node(data)
        node.prev = cur
        cur.next = node

    def length(self):
        length = 0
        cur = self.__head
        while cur is not None:
            length += 1
            cur = cur.next
        return length

    def insert(self, index, data):
        if index <= 0:
            self.add(data)
            return
        if index > self.length() - 1:
            self.append(data)
            return
        cur = self.__head
        for i in range(index - 1):
            cur = cur.next
        node = Node(data)
        node.next = cur.next
        node.prev = cur
        cur.next.prev = node
        cur.next = node

    def is_exist(self, value):
        cur = self.__head
        while cur is not None:
            if cur.data == value:
                return True
            cur = cur.next
        return False

    def index(self, value):
        index = 0
        cur = self.__head
        while cur is not None:
            if cur.data == value:
                return index
            cur = cur.next
            index += 1
        return -1

    def setitem(self, index, value):
        if index < 0:
            raise IndexError
        if index > self.length() - 1:
            raise IndexError
        cur = self.__head
        for i in range(index):
            cur = cur.next
        cur.data = value

    def remove(self, index):
        if index < 0:
            raise IndexError
        if index > self.length() - 1:
            raise IndexError
        cur = self.__head
        for i in range(index):
            cur = cur.next
        if cur == self.__head:
            self.__head = self.__head.next
            if cur.next:
                cur.next.prev = None
            return
        if cur.next is None:
            cur.prev.next = cur.next
            return
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

    def delete(self, value):
        cur = self.__head
        while cur is not None:
            if cur.data == value:
                if cur == self.__head:
                    self.__head = self.__head.next
                    if cur.next:
                        cur.next.prev = None
                    return
                if cur.next is None:
                    cur.prev.next = cur.next
                    return
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return
            cur = cur.next

    def delete_all(self, value):
        cur = self.__head
        while cur is not None:
            if cur.data == value:
                if cur == self.__head:
                    self.__head = self.__head.next
                    if cur.next:
                        cur.next.prev = None
                    self.delete_all(value)
                    return
                if cur.next is None:
                    cur.prev.next = cur.next
                    self.delete_all(value)
                    return
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                self.delete_all(value)
                return
            cur = cur.next


if __name__ == '__main__':
    d = DoubleLinkList()
    print("is_empty: ", d.is_empty())
    d.show()

    d.add(10)
    d.add(100)
    d.append(20)
    d.append(30)
    d.append(40)
    d.show()
    d.insert(1, 200)
    d.show()
    print("链表长度：", d.length())

    print(d.is_exist(200))
    print(d.index(20))
    d.setitem(2, 300)
    d.show()

    d.remove(3)
    d.show()
    d.delete(40)
    d.show()
    d.add(40)
    d.insert(3, 40)
    d.insert(3, 40)
    d.append(40)
    d.append(40)
    d.show()
    d.delete_all(40)
    d.show()
