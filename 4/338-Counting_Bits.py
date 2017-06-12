def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    if num < 0:
        return []
    if num == 0:
        return [0]
    res = [0 for _ in range(num + 1)]
    res[1] = 1
    count = 1
    for i in range(2, num + 1):
        if i == 2 ** count:
            count += 1
            j = 0
        res[i] = 1 + res[j]
        j += 1
    return res

print(countBits(5))