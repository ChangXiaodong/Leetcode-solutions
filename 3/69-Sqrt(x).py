# coding=utf-8
'''
方法一：牛顿法
方法二：二分查找
'''


def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    r = x
    while r * r > x:
        r = (r + x / r) / 2
    return r


def mySqrt1(x):
    if x <= 0:
        return 0
    low = 1
    high = x
    while True:
        middle = (low + high) // 2
        if middle > x // middle:
            high = middle - 1
        else:
            if middle + 1 > x // (middle + 1):
                return middle
            low = middle + 1


print(mySqrt1(5))
