def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 1:
        return x
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    half = myPow(x, n >> 1)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x