'''
方法1：桶排序 O(n)，不是inplace
方法2：不断向后移位,i,j分别记住0和1的下一个插入位置
input:[2, 2, 1, 0, 0, 1, 0]
output:
[2, 2, 1, 0, 0, 1, 0]
[2, 2, 1, 0, 0, 1, 0]
[1, 2, 2, 0, 0, 1, 0]
[0, 1, 2, 2, 0, 1, 0]
[0, 0, 1, 2, 2, 1, 0]
[0, 0, 1, 1, 2, 2, 0]
[0, 0, 0, 1, 1, 2, 2]
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        blucket = [[], [], []]
        for v in nums:
            blucket[v % 10].append(v)
        nums[:] = [b for a in blucket for b in a]
        return nums

    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
            print(nums)


solution = Solution()
print(solution.sortColors2([2, 2, 1, 0, 0, 1, 0]))
