def heap_sort(ary):
    build_max_heap(ary)
    n = len(ary)
    for i in range(n - 1, 0, -1):
        swap(ary, i, 0)
        max_heap(ary, 0, i)
    return ary


def build_max_heap(ary):
    n = len(ary)
    for i in range(int(n / 2), -1, -1):
        max_heap(ary, i, n)
    return ary


def left(i):
    return (i + 1) * 2 - 1


def right(i):
    return (i + 1) * 2


def max_heap(ary, i, size):
    l_sub_tree = left(i)
    r_sub_tree = right(i)
    largest = i
    if l_sub_tree < size and ary[l_sub_tree] > ary[i]:
        largest = l_sub_tree
    if r_sub_tree < size and ary[r_sub_tree] > ary[largest]:
        largest = r_sub_tree
    if largest != i:
        swap(ary, i, largest)
        max_heap(ary, largest, size)
    return ary


def swap(ary, i, j):
    ary[i], ary[j] = ary[j], ary[i]


def sink(ary, k, N):
    while 2 * k <= N:
        j = 2 * k
        if j < N and ary[j] < ary[j + 1]:
            j += 1
        if not ary[k] < ary[j]:
            break
        swap(ary, j, k)
        k = j


def heap_sort2(nums):
    if not nums:
        return []
    n = nums.__len__() - 1
    k = n / 2
    while k >= 1:
        sink(ary, k, n)
        k -= 1
    while n > 1:
        swap(ary, 1, n)
        n -= 1
        sink(ary, 1, n)
    return nums

if __name__ == "__main__":
    ary = [0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 100]
    # [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    print(heap_sort2(ary))
