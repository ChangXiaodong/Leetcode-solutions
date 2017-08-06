# coding=utf-8
'''
方法1：从后至前搜索，遇到0时，搜索0之前的数，若之前的步数能够跳过当前的0，则继续从后向前搜索。若无法跳过当前的0 返回False
注意：当之前的步数虽然没有跳过当前的0但是达到了数组的最后一位也算搜索成功。

方法2：每次保存能够到达的最远index，如果当前遍历的i大于能够到达最远的index，并且还没有到最后一个数，则返回False
'''


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        n = nums.__len__()
        if n > 1 and nums[0] == 0:
            return False
        for i in range(n - 1, -1, -1):
            if nums[i] == 0:
                for j in range(i - 1, -1, -1):
                    if nums[j] + j > i or nums[j] + j == n - 1:
                        break
                    if j == 0:
                        return False
        return True

    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        n = nums.__len__()
        reach = 0
        i = 0
        while i < n and i <= reach:
            reach = max(i + nums[i], reach)
            i += 1
        return i == n

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        n = nums.__len__()
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        if dp[0] == 0 and n > 1:
            return False
        for i in range(1, n):
            dp[i] = max(i + nums[i], dp[i - 1])
            if dp[i] <= i and i != n-1:
                return False
        return True


s = Solution()
print(s.canJump2([2,0,0]))
