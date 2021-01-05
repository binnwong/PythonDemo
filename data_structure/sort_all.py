# coding=utf-8
# def bubble_sort(array):
#     for i in range(1, len(array)):
#         for j in range(0, len(array)-i):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#     return array


# coding=utf-8
# def insertion_sort(array):
#     for i in range(len(array)):
#         cur_index = i
#         while array[cur_index-1] > array[cur_index] and cur_index-1 >= 0:
#             array[cur_index], array[cur_index-1] = array[cur_index-1], array[cur_index]
#             cur_index -= 1
#     return array


# coding=utf-8
# def shell_sort(array):
#     interval = int(len(array)/3)
#     while interval > 0:
#         for i in range(interval, len(array)):
#             cur_index = i - interval
#             while cur_index >= 0 and array[cur_index] > array[cur_index+interval]:
#                 array[cur_index+interval], array[cur_index] = array[cur_index], array[cur_index+interval]
#                 cur_index -= interval
#         interval = int(interval/3)
#     return array


# coding=utf-8
# def selection_sort(array):
#     for i in range(len(array)-1):
#         min_index = i
#         for j in range(i+1, len(array)):
#             if array[j] < array[min_index]:
#                 min_index = j
#         if min_index != i:
#             array[i], array[min_index] = array[min_index], array[i]
#     return array


# coding=utf-8
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     mid_data, left, right = array[start], start, end
#     while left < right:
#         while array[right] >= mid_data and left < right:
#             right -= 1
#         array[left] = array[right]
#         while array[left] < mid_data and left < right:
#             left += 1
#         array[right] = array[left]
#     array[left] = mid_data
#     quick_sort(array, start, left-1)
#     quick_sort(array, left+1, end)


# coding=utf-8
# def merge_sort(array):
#     if len(array) == 1:
#         return array
#     left_array = merge_sort(array[:len(array)//2])
#     right_array = merge_sort(array[len(array)//2:])
#     return merge(left_array, right_array)
#
#
# def merge(left_array, right_array):
#     left_index, right_index, merge_array = 0, 0, list()
#     while left_index < len(left_array) and right_index < len(right_array):
#         if left_array[left_index] <= right_array[right_index]:
#             merge_array.append(left_array[left_index])
#             left_index += 1
#         else:
#             merge_array.append(right_array[right_index])
#             right_index += 1
#     merge_array = merge_array + left_array[left_index:] + right_array[right_index:]
#     return merge_array


# coding=utf-8
# def heap_sort(array):
#     first = len(array) // 2 - 1
#     for start in range(first, -1, -1):
#         # 从下到上，从右到左对每个非叶节点进行调整，循环构建成大顶堆
#         big_heap(array, start, len(array) - 1)
#     for end in range(len(array) - 1, 0, -1):
#         # 交换堆顶和堆尾的数据
#         array[0], array[end] = array[end], array[0]
#         # 重新调整完全二叉树，构造成大顶堆
#         big_heap(array, 0, end - 1)
#     return array
#
#
# def big_heap(array, start, end):
#     root = start
#     # 左孩子的索引
#     child = root * 2 + 1
#     while child <= end:
#         # 节点有右子节点，并且右子节点的值大于左子节点，则将child变为右子节点的索引
#         if child + 1 <= end and array[child] < array[child + 1]:
#             child += 1
#         if array[root] < array[child]:
#             # 交换节点与子节点中较大者的值
#             array[root], array[child] = array[child], array[root]
#             # 交换值后，如果存在孙节点，则将root设置为子节点，继续与孙节点进行比较
#             root = child
#             child = root * 2 + 1
#         else:
#             break


# if __name__ == '__main__':
#     array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
#     print(heap_sort(array))


# coding=utf-8
# def counting_sort(array):
#     if len(array) < 2:
#         return array
#     max_num = max(array)
#     count = [0] * (max_num + 1)
#     for num in array:
#         count[num] += 1
#     new_array = list()
#     for i in range(len(count)):
#         for j in range(count[i]):
#             new_array.append(i)
#     return new_array


# if __name__ == '__main__':
#     array = [5, 7, 3, 7, 2, 3, 2, 5, 9, 5, 7, 6]
#     print(counting_sort(array))


# coding=utf-8
# def bucket_sort(array):
#     min_num, max_num = min(array), max(array)
#     bucket_num = (max_num-min_num)//3 + 1
#     buckets = [[] for _ in range(int(bucket_num))]
#     for num in array:
#         buckets[int((num-min_num)//3)].append(num)
#     new_array = list()
#     for i in buckets:
#         for j in sorted(i):
#             new_array.append(j)
#     return new_array
#
#
# if __name__ == '__main__':
#     array = [5, 7, 3, 7, 2, 3, 2, 5, 9, 5, 7, 8]
#     print(bucket_sort(array))


# coding=utf-8
def radix_sort(array):
    max_num = max(array)
    place = 1
    while max_num >= 10**place:
        place += 1
    for i in range(place):
        buckets = [[] for _ in range(10)]
        for num in array:
            radix = int(num/(10**i) % 10)
            buckets[radix].append(num)
        j = 0
        for k in range(10):
            for num in buckets[k]:
                array[j] = num
                j += 1
    return array


if __name__ == '__main__':
    array = [25, 17, 33, 17, 22, 13, 32, 15, 9, 25, 27, 18, 100]
    print(radix_sort(array))
