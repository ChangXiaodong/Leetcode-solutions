# coding=utf-8
'''
每次dfs时传入一个index， 取数只能从index和index之后取
'''
class Solution(object):
    def dfs(self, nums, target, buf, res, index):
        if sum(buf) == target:
            if buf not in res:
                res.append(buf[:])
            return
        if sum(buf) > target:
            return
        for i in range(index, len(nums)):
            buf.append(nums[i])
            self.dfs(nums, target, buf, res, i)
            buf.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return
        res = []
        self.dfs(candidates, target, [], res, 0)
        return res


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
