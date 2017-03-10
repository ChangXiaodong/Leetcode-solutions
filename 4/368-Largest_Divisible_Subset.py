#coding=utf-8
'''
dp存储到x时最大子数组长度
pre存储对应的最大下标
状态转移方程：
dp[x] = max(dp[x], dp[y]+1)  0<=y<x and nums[x] % nums[y] == 0
'''

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
        return []
    nums = sorted(nums)
    n = len(nums)
    dp, pre = [1] * n, [None] * n
    for x in range(n):
        for y in range(x):
            if nums[x] % nums[y] == 0 and dp[y] + 1 > dp[x]:
                dp[x] = dp[y] + 1
                pre[x] = y
    max_index = dp.index(max(dp))
    ans = []
    while max_index is not None:
        ans += nums[max_index],
        max_index = pre[max_index]

    return ans

print(largestDivisibleSubset([1, 7, 4, 8]))
