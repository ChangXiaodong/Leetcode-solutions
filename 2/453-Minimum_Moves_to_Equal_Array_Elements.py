'''
方法1：数学方法
sum 是原始nums的和
n是nums长度
x是最终相同的那个数字
m是移动步数
min是nums中最小的数字
sum + m * (n - 1) = x * n
并且x = min + m
所以sum - minNum * n = m
'''
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * nums.__len__()


solution = Solution()
print(solution.minMoves([1,2147483647]))
