def PredictTheWinner(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i][i] = nums[i]
    for i in range(1, len(nums)):
        j = 0
        while j + i < len(nums):
            dp[j][j + i] = max(nums[j + i] - dp[j][j + i - 1], nums[j] - dp[j + 1][j + i])
            j += 1
    return dp[0][-1] >= 0