class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        index = (nums.__len__() + 1) // 2
        i = 1
        for j in range(index, nums.__len__()):
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
        return nums


solution = Solution()
print(solution.wiggleSort([1, 5, 1, 1, 6, 4]))
