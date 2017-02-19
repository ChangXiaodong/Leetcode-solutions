def multiply(arr):
    if not arr:
        return
    length = len(arr)
    new_arr = [1 for _ in range(length)]

    for i in range(1, length):
        new_arr[i] = new_arr[i - 1] * arr[i - 1]
    temp = 1
    for i in range(length - 2, 0, -1):
        temp *= arr[i + 1]
        new_arr[i] *= temp
    return new_arr


print(multiply([1, 2, 3, 4, 5]))
