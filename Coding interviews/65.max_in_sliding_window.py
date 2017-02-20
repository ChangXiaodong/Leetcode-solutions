def max_in_window(arr, size):
    if not arr:
        return
    if len(arr) < size:
        return
    quene = []

    max_num = 0
    for i, v in enumerate(arr):
        if quene and i - size > quene[0] - 1:
            quene.pop(0)
            max_num = arr[quene[0]]
        length = len(quene)
        j = 0
        while j < length:
            if v > arr[quene[j]]:
                quene.pop(j)
                length -= 1
            else:
                j += 1
        if v > max_num:
            quene.append(i)
            max_num = v
        else:
            quene.append(i)
        print(arr[quene[0]])


max_in_window([2, 3, 4, 2, 6, 2, 5, 1], 3)
