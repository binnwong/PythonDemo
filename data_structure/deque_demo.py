# coding=utf-8
import collections


queue = collections.deque()
queue.append('a')
queue.append('b')
queue.append('c')
# print(queue)
queue.appendleft('A')
queue.appendleft('B')
# print(queue)

queue.extend(['D', 'E'])
# queue.extend(['DE'])
queue.extendleft(['c', 'd'])
# print(queue)

queue.insert(3, 'T')
# print(queue)


print(queue.pop())
print(queue.popleft())
# print(queue)


# queue_b = queue.copy()
# print(queue)
# print(queue_b)
# print(id(queue))
# print(id(queue_b))


# print(queue.count('b'))
queue.append('b')
# print(queue.count('b'))
# print(queue.count('z'))
# print(queue.index('T'))
# print(queue.index('O'))


# print(queue)
queue.reverse()
# print(queue)
queue.rotate(3)
# print(queue)


print(queue)
queue.remove('b')
# queue.remove('O')
print(queue)
queue.clear()
print(queue)


que = collections.deque(maxlen=5)
que.extend(['a', 'b', 'c', 'd', 'e'])
print(que)
que.append('F')
print(que)
que.appendleft('A')
print(que)
