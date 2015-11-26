__author__ = 'Changxiaodong'
import time
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i<len(nums):
            if val == nums[i]:
                nums.pop(i)
            else:
                i+=1
            print nums
        return i

    def removeElement1(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
            print nums
        return start

if __name__ == "__main__":
    start = time.clock()
    test = Solution()
    print test.removeElement([3,3,4,3,3],3)
    print time.clock() - start