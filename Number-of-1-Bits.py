__author__ = 'Changxiaodong'
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        for i in range(32):
            if n & 0x01 == 1:
                num+=1
            n = n >> 1
        return num