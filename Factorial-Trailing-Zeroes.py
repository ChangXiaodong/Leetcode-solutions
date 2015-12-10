class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<5:
            return 0

        count = 0
        while n>=5:
            count += n/5
            n/=5
        return count

    def trailingZeroes1(self, n):
        if n<5:
            return 0
        return n/5+self.trailingZeroes1(n/5)