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
