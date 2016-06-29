__author__ = 'Changxiaodong'
'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Hint:

Try two pointers.
Did you use the property of "the order of elements can be changed"?
What happens when the elements to remove are rare?
'''
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