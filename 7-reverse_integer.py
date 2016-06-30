'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    num = abs(x)
    y = num % 10
    num /= 10
    while num != 0:
        y = y * 10 + num % 10
        num /= 10
    if y > int(pow(2, 32)/2) - 1:  #the boundary of the integer is -2147483648 to 2147483647
        y = 0
    if x >= 0:
        return y
    else:
        return -y
