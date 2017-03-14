import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums
        self.nums = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.original)):
            j = random.randint(0, len(self.original) - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums