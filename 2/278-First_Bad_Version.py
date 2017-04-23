# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low < high:
            middle = (low + high) / 2
            if isBadVersion(middle) == False:
                low = middle + 1
            else:
                high = middle
        return low
