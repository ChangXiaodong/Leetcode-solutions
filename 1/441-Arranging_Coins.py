class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        i = 1
        while n >= i:
            n -= i
            i += 1
            cnt += 1
        return cnt