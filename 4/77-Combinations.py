# coding=utf-8
'''
注意遍历的range范围，在k后面的值不需要遍历
'''
class Solution(object):
    def dfs(self, n, k, buf, index):
        if len(buf) == k:
            self.res.append(buf[:])
            return
        for i in range(index, n + len(buf) - k + 1):
            buf.append(i+1)
            self.dfs(n, k, buf, i+1)
            buf.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n <= 0 or k <=0:
            return []
        self.res = []
        self.dfs(n, k, [], 0)
        return self.res

solution = Solution()
print(solution.combine(20, 16))
