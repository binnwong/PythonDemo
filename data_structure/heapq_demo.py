# coding=utf-8
import heapq


# array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
# heap = []
# for num in array:
#     heapq.heappush(heap, num)
# print("array:", array)
# print("heap: ", heap)
#
# heapq.heapify(array)
# print("array:", array)


# array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
# heap = []
# for num in array:
#     heapq.heappush(heap, num)
# print(heap[0])
# # print(heapq.heappop(heap))
# heap_sort = [heapq.heappop(heap) for _ in range(len(heap))]
# print("heap sort result: ", heap_sort)


# array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
# heapq.heapify(array)
# print(heapq.nlargest(100, array))
# print(heapq.nsmallest(3, array))


# array_a = [10, 7, 15, 8]
# array_b = [17, 3, 8, 20, 13]
# heapq.heapify(array_a)
# heapq.heapify(array_b)
# array_merge = heapq.merge(sorted(array_a), sorted(array_b))
# print("merge result:", list(array_merge))


array_c = [10, 7, 15, 8]
heapq.heapify(array_c)
print("before:", array_c)
# 先push再pop
item = heapq.heappushpop(array_c, 5)
print("after: ", array_c)
print(item)

array_d = [10, 7, 15, 8]
heapq.heapify(array_d)
print("before:", array_d)
# 先pop再push
item = heapq.heapreplace(array_d, 5)
print("after: ", array_d)
print(item)
