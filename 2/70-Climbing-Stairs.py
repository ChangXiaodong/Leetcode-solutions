__author__ = 'Changxiaodong'
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
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
            steps = bbefore + before
            for i in range(n-1):
                bbefore = steps
                steps += before
                before = bbefore
            return steps