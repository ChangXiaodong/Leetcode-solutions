# coding=utf-8
'''
方法1：哈希表，注意k为0 的时候
方法2：双指针
每次j从i+1开始遍历，找到nums[j]不小于nums[i]的数， 看num[i],num[j]的差是否等于k
然后把i向前挪， 挪到下个不重复的数字重新开始遍历。
'''
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or len(nums) < 2:
            return 0
        res = 0

        table = {}
        for v in nums:
            table[v] = table.get(v, 0) + 1
        for key, v in table.items():
            if k == 0:
                if v >= 2:
                    res += 1
            else:
                if table.get(key + k, "null") != "null":
                    res += 1
        return res

    def findPairs1(self, nums, k):
        nums.sort()
        i = 0
        j = 0
        res = 0
        while i < len(nums):
            j = max(j, i + 1)
            while j < len(nums) and nums[j] - nums[i] < k:
                j += 1
            if j < len(nums) and nums[j] - nums[i] == k:
                res += 1
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res


solution = Solution()
print(solution.findPairs1([3, 1, 4, 4, 5], 2))
