def subSetSum(nums, S):
    dp = [0] * (S + 1)
    dp[0] = 1
    for v in nums:
        i = S
        while i >= v:
            dp[i] += dp[i - v]
            i -= 1
    return dp[S]


def findTargetSumWays(nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    if not nums:
        return
    sums = sum(nums)
    if S > sums:
        return 0
    p2 = S + sums
    if p2 % 2 != 0:
        return 0
    p_target = p2 / 2
    return subSetSum(nums, p_target)


# print(findTargetSumWays([1, 1, 1, 1, 1], 3))
print(subSetSum([2, 2, 2], 4))
