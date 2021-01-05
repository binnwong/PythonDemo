# coding=utf-8
class SequenceList(object):

    def __init__(self, max=10):
        self.max = max
        self.data = [None] * self.max
        self.num = 0

    def is_empty(self):
        return self.num is 0

    def is_full(self):
        return self.num is self.max

    def show(self):
        print('<', end='')
        for i in range(0, self.num):
            if i != self.num-1:
                print(self.data[i], end=',')
            else:
                print(self.data[i], end='')
        print('>')

    def add(self, value):
        for j in range(self.num, 0, -1):
            self.data[j] = self.data[j-1]
        self.data[0] = value
        self.num += 1

    def append(self, value):
        self.data[self.num] = value
        self.num += 1

    def insert(self, i, value):
        if not isinstance(i, int):
            raise TypeError
        if i < 0:
            self.add(value)
        if i > self.num:
            self.append(value)
        for j in range(self.num, i, -1):
            self.data[j] = self.data[j-1]
        self.data[i] = value
        self.num += 1

    def count(self):
        return self.num

    def is_exist(self, value):
        for j in range(self.num):
            if self.data[j] == value:
                return True
        else:
            return False

    def index(self, value):
        for j in range(self.num):
            if self.data[j] == value:
                return j
        else:
            return -1

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError
        if 0 <= item < self.num:
            return self.data[item]
        else:
            raise IndexError

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError
        if 0 <= key < self.num:
            self.data[key] = value
        else:
            raise IndexError

    def remove(self, i):
        if not isinstance(i, int):
            raise TypeError
        if i < 0 or i >= self.num:
            raise IndexError
        for j in range(i, self.num):
            if j == self.num-1:
                self.data[j] = None
            else:
                self.data[j] = self.data[j+1]
        self.num -= 1

    def delete(self, value):
        for i in range(self.num):
            if self.data[i] == value:
                self.remove(i)
                return

    def delete_all(self, value):
        for i in range(self.num):
            if self.data[i] == value:
                self.remove(i)
                self.delete_all(value)


if __name__ == '__main__':
    s = SequenceList()
    print("is_empty: ", s.is_empty())
    print("is_full: ", s.is_full())
    s.show()
    s.add(1)
    s.add(10)
    s.append(2)
    s.append(3)
    s.append(4)
    s.show()
    s.insert(1, 20)
    s.show()
    print("顺序表长度：", s.count())
    s.show()
    print(s.is_exist(200))
    print(s.index(20))
    print(s.__getitem__(1))
    print(s[1])
    s[2] = 30
    s.__setitem__(3, 40)
    s.show()
    s.remove(5)
    s.show()
    s.append(4)
    s.append(4)
    s.append(4)
    s.append(4)
    s.append(4)
    print("is_full: ", s.is_full())
    s.show()
    print("s的长度：", s.count())
    # s.remove(9)
    s.delete(4)
    s.show()
    s.delete_all(4)
    s.show()
