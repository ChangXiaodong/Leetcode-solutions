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
    left = S
    nums.sort()
    nums.reverse()
    i = 0
    count = 0
    while i < nums.__len__():
        if left < nums[i]:
            i += 1
        else:
            left -= nums[i]
            nums.pop(i)
        if left == 0:
            count += 1
            left = S
    return count


print(findTargetSumWays([1, 1, 1, 1, 1], 3))
print(subSetSum([1, 1, 1, 1, 1], 4))
