def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    i = 1
    while i <= num:
        i = i << 1
    return num ^ (i - 1)


print(findComplement(2))
