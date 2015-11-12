__author__ = 'Changxiaodong'
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            bbefore = 0
            before = 1
            steps = 0
            steps = bbefore + before
            for i in range(n-1):
                bbefore = steps
                steps += before
                before = bbefore
            return steps