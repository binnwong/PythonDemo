# coding=utf-8
class SequenceStack(object):

    def __init__(self):
        self.__members = list()

    def is_empty(self):
        return not len(self.__members)

    def show(self):
        if self.is_empty():
            print('空栈')
            return
        for member in self.__members:
            print('|' + member, end='')
        print()

    def push(self, data):
        self.__members.append(data)

    def pop(self):
        if self.is_empty():
            return
        return self.__members.pop()

    def length(self):
        return len(self.__members)

    def check(self):
        if self.is_empty():
            return
        return self.__members[len(self.__members)-1]


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkStack(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return not self.__head

    def show(self):
        if self.is_empty():
            print('空栈')
            return
        cur = self.__head
        while cur is not None:
            if cur.next is not None:
                print('|' + cur.data, end='')
            else:
                print('|' + cur.data)
            cur = cur.next

    def push(self, data):
        node = Node(data)
        if self.is_empty():
            self.__head = node
            return
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def pop(self):
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

    def check(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        return cur.data


if __name__ == '__main__':
    ss = SequenceStack()
    print("is_empty: ", ss.is_empty())
    ss.show()

    ss.push('a')
    ss.push('b')
    ss.push('c')
    ss.push('d')
    ss.push('e')
    ss.show()
    print(ss.pop())
    ss.show()

    print("sequence stack length: ", ss.length())
    print("top member is: ", ss.check())

    ls = LinkStack()
    print("is_empty: ", ls.is_empty())
    ls.show()

    ls.push('A')
    ls.push('B')
    ls.push('C')
    ls.push('D')
    ls.push('E')
    ls.show()
    print(ls.pop())
    ls.show()

    print("link stack length: ", ls.length())
    print("top member is: ", ls.check())
