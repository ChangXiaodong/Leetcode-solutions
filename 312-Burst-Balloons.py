'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''
def maxCoins_Bottomup(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]  # build the complete array
    n = len(nums)
    dp = [[0] * n for _ in xrange(n)]

    for gap in xrange(2, n):
        for i in xrange(n - gap):
            j = i + gap
            for k in xrange(i + 1, j):
                dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
    return dp[0][n - 1]


def maxCoins_Topdown(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    def get_max(i, j):
        if dp[i][j]:
            return dp[i][j]
        for k in range(i+1, j):
            dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + get_max(i, k) + get_max(k, j))
        return dp[i][j]

    return get_max(0, n - 1)


print maxCoins_Bottomup([3, 1, 5, 8])
print maxCoins_Topdown([3, 1, 5, 8])
