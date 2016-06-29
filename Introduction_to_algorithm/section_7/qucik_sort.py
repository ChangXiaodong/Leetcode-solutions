import sys
sys.setrecursionlimit(100000000)

def partition(ary, p, r):
    primary_value = ary[r]
    i = p - 1
    for j in range(p, r):
        if ary[j] <= primary_value:
            i += 1
            ary[i], ary[j] = ary[j], ary[i]
    ary[r], ary[i + 1] = ary[i + 1], ary[r]
    return i + 1


def q_sort(ary, p, r):
    if p < r:
        q = partition(ary, p, r)
        q_sort(ary, p, q - 1)
        q_sort(ary, q + 1, r)
    return ary


def quick_sort(ary):
    return q_sort(ary, 0, len(ary)-1)
