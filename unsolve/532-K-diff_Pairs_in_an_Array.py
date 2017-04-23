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
        index1 = 0
        index2 = 1
        nums.sort()
        while index2 < len(nums):
            if nums[index2] - nums[index1] < k:
                index2 += 1
            elif nums[index2] - nums[index1] > k:
                index1 += 1
            else:
                res += 1
                index1 += 1
                index2 += 1
                while index1 < len(nums) - 1 and nums[index1] == nums[index1 + 1]:
                    index1 += 1
                    index2 += 1
            if index1 == index2:
                index2 += 1
        return res

solution = Solution()
print(solution.findPairs([6,3,5,7,2,3,3,8,2,4], 2))
