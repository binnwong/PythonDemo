# coding=utf-8
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class SingleCycleLinkList(object):

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return not self.__head

    def show(self):
        if self.is_empty():
            print('空链表')
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.data, end=' → ')
            cur = cur.next
        print(cur.data, '→ ')

    def add(self, data):
        node = Node(data)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        node.next = self.__head
        self.__head = node

    def append(self, data):
        if self.is_empty():
            self.add(data)
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        node = Node(data)
        cur.next = node
        node.next = self.__head

    def length(self):
        if self.is_empty():
            return 0
        length = 1
        cur = self.__head
        while cur.next != self.__head:
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
        for i in range(index-1):
            cur = cur.next
        node = Node(data)
        node.next = cur.next
        cur.next = node

    def is_exist(self, value):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.data == value:
                return True
            cur = cur.next
        if cur.data == value:
            return True
        return False

    def index(self, value):
        if self.is_empty():
            return -1
        index = 0
        cur = self.__head
        while cur.next != self.__head:
            if cur.data == value:
                return index
            cur = cur.next
            index += 1
        if cur.data == value:
            return index
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
        prev = None
        for i in range(index):
            prev = cur
            cur = cur.next
        if cur == self.__head:
            prev = self.__head
            while prev.next != self.__head:
                prev = prev.next
            if prev == self.__head:
                self.__head = None
                return
            prev.next = self.__head.next
            self.__head = self.__head.next
            return
        prev.next = cur.next

    def delete(self, value):
        cur = self.__head
        prev = None
        while cur.next != self.__head:
            if cur.data == value:
                if cur == self.__head:
                    prev = self.__head
                    while prev.next != self.__head:
                        prev = prev.next
                    prev.next = cur.next
                    self.__head = cur.next
                    return
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
        if cur.data == value:
            if cur == self.__head:
                self.__head = None
                return
            prev.next = cur.next
            return

    def delete_all(self, value):
        cur = self.__head
        prev = None
        while cur.next != self.__head:
            if cur.data == value:
                if cur == self.__head:
                    prev = self.__head
                    while prev.next != self.__head:
                        prev = prev.next
                    prev.next = cur.next
                    self.__head = cur.next
                    self.delete_all(value)
                    return
                prev.next = cur.next
                self.delete_all(value)
                return
            prev = cur
            cur = cur.next
        if cur.data == value:
            if cur == self.__head:
                self.__head = None
                return
            prev.next = cur.next
            self.delete_all(value)
            return


if __name__ == '__main__':
    s = SingleCycleLinkList()
    print("is_empty: ", s.is_empty())
    s.show()

    s.add(1)
    s.add(10)
    s.append(2)
    s.append(3)
    s.append(4)
    s.show()
    s.insert(1, 20)
    s.show()
    print("链表长度：", s.length())

    print(s.is_exist(100))
    print(s.index(20))
    s.setitem(2, 30)
    s.show()

    s.remove(3)
    s.show()
    s.delete(4)
    s.show()
    s.add(4)
    s.insert(3, 4)
    s.insert(3, 4)
    s.append(4)
    s.append(4)
    s.show()
    s.delete_all(4)
    s.show()
