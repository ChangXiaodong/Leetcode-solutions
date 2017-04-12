# coding=utf-8
'''
遍历数字，找到这个数字之前的局部最大，和局部最小。然后与本数字乘积，更新局部最大和局部最小。在局部最大中找到全局最大
'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = nums.__len__()
        max_pre = nums[0]
        min_pre = nums[0]
        max_product = nums[0]
        for i in range(1, n):
            max_num = max([max_pre * nums[i], min_pre * nums[i], nums[i]])
            min_num = min([max_pre * nums[i], min_pre * nums[i], nums[i]])
            max_product = max(max_num, max_product)
            max_pre = max_num
            min_pre = min_num
        return max_product


solution = Solution()
print(solution.maxProduct([2, 3, -2, 4]))
