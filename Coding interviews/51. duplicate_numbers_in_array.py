def duplicate_numbers(arr):
    if not arr:
        return
    length = len(arr)
    for v in arr:
        if v < 0 or v > length-1:
            return
    for i in range(length):
        while i != arr[i]:
            if arr[i] == arr[arr[i]]:
                return arr[i]
            index = arr[i]
            arr[i], arr[index] = arr[index], arr[i]


print(duplicate_numbers([2, 3, 1, 0, 2, 5, 3]))
