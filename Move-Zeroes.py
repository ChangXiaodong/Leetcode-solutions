__author__ = 'Changxiaodong'
import time
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
        print nums

if __name__ == "__main__":
    start = time.clock()
    test = Solution()
    test.moveZeroes([0,0,1])
    print time.clock() - start