def getMoneyAmount(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for j in range(2, n + 1):
        for i in range(j - 1, 0, -1):
            global_min = float('inf')
            for k in range(i + 1, j):
                local_max = k + max(dp[i][k - 1], dp[k + 1][j])
                global_min = min(global_min, local_max)
            dp[i][j] = i if i + 1 == j else global_min
    return dp[1][n]


print(getMoneyAmount(4))
