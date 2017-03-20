'''
方法1：遍历
方法2：奇葩二分查找
这个查找能够成立的的条件是num[-1] = num[n] = -∞，并且多个峰值返回任意一个就可以
比如输入是[1,2,30,2,5,6,7]，最大峰值index为2，但实际返回6
'''
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        n = nums.__len__()
        nums.append(float("-inf"))
        for i in range(1, n):
            if nums[i-1] < nums[i] and nums[i] > nums[i + 1]:
                return i
        return 0
    def findPeakElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        high = nums.__len__() - 1
        low = 0
        while low < high:
            mid1 = (low + high) / 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                low = mid2
            else:
                high = mid1
        return low