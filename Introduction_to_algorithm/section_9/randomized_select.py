import random


def partition(ary, p, r):
    primary_value = ary[r]
    i = p - 1
    for j in range(p, r):
        if ary[j] <= primary_value:
            i += 1
            ary[i], ary[j] = ary[j], ary[i]
    ary[r], ary[i + 1] = ary[i + 1], ary[r]
    return i + 1


def random_partition(ary, p, r):
    rand = random.randint(p, r)
    ary[rand], ary[r] = ary[r], ary[rand]
    return rand, partition(ary, p, r)


def randomized_select(ary, p, r, i):
    if p == r:
        return ary[p]
    random, q = random_partition(ary, p, r)
    k = q - p + 1
    if k == i:
        return ary[q]
    elif i < k:
        return randomized_select(ary, p, q - 1, i)
    else:
        return randomized_select(ary, q + 1, r, i - k)


def find_ist_number(ary, i):
    return randomized_select(ary, 0, len(ary) - 1, i)


if __name__ == "__main__":
    print(find_ist_number(
        [1, 4, 7, 2, 5, 8, 3, 6, 9, 0],
        8
    ))
