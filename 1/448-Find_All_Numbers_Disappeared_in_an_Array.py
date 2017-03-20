class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = nums.__len__()
        for i in range(n):
            index = nums[i]
            if index < -n:
                index  = abs(index + n) - 1
            else:
                index = abs(index) - 1
            if nums[index] < 0:
                nums[index] = nums[index] - n
            else:
                nums[index] = -nums[index]
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res