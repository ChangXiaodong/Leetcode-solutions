class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        buf = nums[0]
        i = 0
        while i < len(nums) - 1:
            if buf == nums[i + 1]:
                nums.pop(i + 1)
            else:
                buf = nums[i + 1]
                i += 1
        return len(nums)