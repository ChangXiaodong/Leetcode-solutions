__author__ = 'Changxiaodong'
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
