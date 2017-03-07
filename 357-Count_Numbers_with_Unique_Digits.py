def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 1
    if n == 1:
        return 10
    res = 10
    for i in range(2, n + 1):
        buf = 9
        for j in range(2, i + 1):
            buf *= 9 - j + 2
        res += buf
    return res


print(countNumbersWithUniqueDigits(9))
