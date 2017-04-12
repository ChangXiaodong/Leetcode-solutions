# coding=utf-8
'''
排序：然后将大的数在偶数位插入，小的数在奇数位插入
'''
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        snums = sorted(nums)
        for x in range(1, size, 2) + range(0, size, 2):
            nums[x] = snums.pop()


solution = Solution()
print(solution.wiggleSort([1, 5, 1, 1, 6, 4]))
