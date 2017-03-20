class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        buf = 0
        for v in nums:
            if v == 1:
                buf += 1
            else:
                res = max(buf, res)
                buf = 0
        res = max(buf, res)
        return res

solution  = Solution()
print(solution.findMaxConsecutiveOnes([1]))