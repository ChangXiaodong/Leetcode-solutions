def calculateMinimumHP(dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    if not dungeon:
        return
    row = dungeon.__len__()
    col = dungeon[0].__len__()

    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[row - 1][col - 1] = max(1, 1 - dungeon[row - 1][col - 1])
    for r in range(row - 2, -1, -1):
        dp[r][col - 1] = max(1, dp[r + 1][col - 1] - dungeon[r][col - 1])
    for c in range(col - 2, -1, -1):
        dp[row - 1][c] = max(1, dp[row - 1][c + 1] - dungeon[row - 1][c])

    for r in range(row - 2, -1, -1):
        for c in range(col - 2, -1, -1):
            dp[r][c] = min(max(1, dp[r + 1][c] - dungeon[r][c]), max(1, dp[r][c + 1] - dungeon[r][c]))
    return dp[0][0]


print(calculateMinimumHP([
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]))
