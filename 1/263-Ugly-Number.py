__author__ = 'Changxiaodong'
'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        else:
            if num == 0:
                return True
            elif num%2 == 0:
                num /= 2
            elif num%3 == 0:
                num /= 3
            elif num%5 == 0:
                num /= 5
            else:
                return False
            return self.isUgly(num)