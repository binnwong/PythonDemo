# coding=utf-8
class SequenceDoubleQueue(object):

    def __init__(self):
        self.__members = list()

    def is_empty(self):
        return not len(self.__members)

    def show(self):
        if self.is_empty():
            print('双端队列为空')
            return
        for member in self.__members:
            if self.__members.index(member) != len(self.__members)-1:
                print(member, end='|')
            else:
                print(member)

    def head_enter(self, data):
        self.__members.insert(0, data)

    def end_enter(self, data):
        self.__members.append(data)

    def head_outer(self):
        if self.is_empty():
            return
        return self.__members.pop(0)

    def end_outer(self):
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


class LinkDoubleQueue(object):

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return not self.__head

    def show(self):
        if self.is_empty():
            print('双端队列为空')
            return
        cur = self.__head
        while cur is not None:
            if cur.next is not None:
                print(cur.data, end='|')
            else:
                print(cur.data)
            cur = cur.next

    def head_enter(self, data):
        node = Node(data)
        node.next = self.__head
        self.__head = node

    def end_enter(self, data):
        if self.is_empty():
            self.head_enter(data)
            return
        node = Node(data)
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def head_outer(self):
        if self.is_empty():
            return
        cur = self.__head
        self.__head = self.__head.next
        return cur.data

    def end_outer(self):
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
    sdq = SequenceDoubleQueue()
    print("is_empty: ", sdq.is_empty())
    sdq.show()

    sdq.head_enter('x')
    sdq.head_enter('y')
    sdq.head_enter('z')
    sdq.end_enter(10)
    sdq.end_enter(20)
    sdq.end_enter(30)
    sdq.show()
    print(sdq.head_outer())
    print(sdq.end_outer())
    sdq.show()

    print("sequence double queue length: ", sdq.length())
    print("index member is: ", sdq.check(2))

    ldq = LinkDoubleQueue()
    print("is_empty: ", ldq.is_empty())
    ldq.show()

    ldq.head_enter('X')
    ldq.head_enter('Y')
    ldq.head_enter('Z')
    ldq.end_enter(100)
    ldq.end_enter(200)
    ldq.end_enter(300)
    ldq.show()
    print(ldq.head_outer())
    print(ldq.end_outer())
    ldq.show()

    print("link queue length: ", ldq.length())
    print("index member is: ", ldq.check(2))
