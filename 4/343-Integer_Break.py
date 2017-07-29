def integerBreak(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 2:
        return 1
    if n == 3:
        return 2
    numof3 = n // 3 - 1
    left = n - numof3 * 3
    if left == 4:
        return pow(3, numof3) * 4
    elif left == 5:
        return pow(3, numof3) * 6
    else:
        return pow(3, numof3) * 3


def integerBreak1(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 2:
        return 1
    if n == 3:
        return 2
    product = 1
    while n > 4:
        product *= 3
        n -= 3
    product *= n
    return product

print(integerBreak(10))
print(integerBreak1(10))
