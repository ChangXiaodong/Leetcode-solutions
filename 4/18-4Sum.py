class Solution(object):
    def sum_3(self, nums, target):
        res = []
        for i in range(len(nums) - 1):
            k = len(nums) - 1
            j = i + 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                _3_sum = nums[i] + nums[j] + nums[k]
                if _3_sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                if _3_sum > target:
                    k -= 1
                else:
                    j += 1
        return res

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            res_temp = self.sum_3(nums[i + 1:], target - nums[i])
            if not res_temp:
                continue
            for r in res_temp:
                r.insert(0, nums[i])
                res.append(r)
        return res


s = Solution()
print(s.fourSum([-1, -5, -5, -3, 2, 5, 0, 4], 0))
