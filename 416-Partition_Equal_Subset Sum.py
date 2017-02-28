def subSetSum(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for v in nums:
        i = target
        while i >= v:
            dp[i] += dp[i - v]
            i -= 1
    return dp[target] != 0


def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    return subSetSum(nums, target)

print(canPartition([1,5,11,5]))
