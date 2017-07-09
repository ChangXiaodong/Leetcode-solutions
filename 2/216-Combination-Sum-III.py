class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        self.dfs(xrange(1, 10), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0:  # backtracking
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, path + [nums[i]], res)


sl = Solution()
print(sl.combinationSum3(3, 7))
