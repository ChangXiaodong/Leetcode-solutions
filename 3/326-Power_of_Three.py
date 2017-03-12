def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    # 1162261467 is 3 ^ 19, 3 ^ 20 is bigger than int
    return n > 0 and 1162261467 % n == 0
