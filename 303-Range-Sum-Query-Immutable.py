'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = []
        if len(nums) > 1:
            self.nums.append(nums[0])
            for i in range(1,len(nums)):
                self.nums.append(self.nums[i-1] + nums[i])
        else:
            self.nums = nums


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i-1]


if __name__ == "__main__":
    test = NumArray([-2,0,3,-5,2,-1])
    print test.nums
    print test.sumRange(0,5)

