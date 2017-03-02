def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    if m * n <= 0:
        return 0
    if m == 1:
        return 1
    if n == 1:
        return 1
    dp = [[0 for _ in range(n)] for _ in range(m)]
    print(dp)
    for r in range(m):
        dp[r][0] = 1
    for c in range(n):
        dp[0][c] = 1
    dp[0][0] = 0
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[m - 1][n - 1]


print(uniquePaths(1, 2))
