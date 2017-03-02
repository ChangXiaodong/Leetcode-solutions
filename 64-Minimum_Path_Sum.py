def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid:
        return
    row = grid.__len__()
    col = grid[0].__len__()
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = grid[0][0]
    for r in range(1, row):
        dp[r][0] = dp[r - 1][0] + grid[r][0]
    for c in range(1, col):
        dp[0][c] = dp[0][c - 1] + + grid[0][c]
    for r in range(1, row):
        for c in range(1, col):
            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
    return dp[row-1][col-1]


print(minPathSum([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]))
