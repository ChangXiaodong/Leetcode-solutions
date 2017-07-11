__author__ = 'Changxiaodong'
'''
Given an integer, write a function to determine if it is a power of two.
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n==1:
            return True
        if n/2==1 and n%2==0:
            return True
        elif n%2 == 0:
            return self.isPowerOfTwo(n/2)
        else:
            return False
