def guess(n):
    pass

def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    high = n
    low = 0
    middle = (high + low) // 2
    res = guess(middle)
    while res != 0:
        if res == -1:
            high = middle - 1
        elif res == 1:
            low = middle + 1
        middle = (high + low) // 2
        res = guess(middle)
    return middle
