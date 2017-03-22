class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        low = 0
        high = nums.__len__() - 1
        start = -2
        end = 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                start = mid
                end = mid
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < nums.__len__() and nums[end] == target:
                    end += 1
                break
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [start + 1, end - 1]