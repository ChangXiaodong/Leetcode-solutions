def heap_sort(A):
    build_max_heap(A)
    n = len(A)
    for i in range(n - 1, 0, -1):
        swap(A, i, 0)
        max_heap(A, 0, n - 1)
        print A
    return A


def build_max_heap(A):
    n = len(A)
    for i in range(n / 2, -1, -1):
        max_heap(A, i, n)
    print A



def max_heap(A, i, size):
    largest = i
    if 2 * i < size and A[2 * i] > A[i]:
        largest = 2 * i
    if 2 * i + 1 < size and A[2 * i + 1] > A[largest]:
        largest = 2 * i + 1
    if largest != i:
        swap(A, i, largest)
        max_heap(A, largest, size)


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


print heap_sort([1, 2, 3, 4, 5])
