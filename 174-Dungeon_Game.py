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
    dp[0][0] = dungeon[0][0]
    for r in range(1, row):
        dp[r][0] = dp[r - 1][0] + dungeon[r][0]
    for c in range(1, col):
        dp[0][c] = dp[0][c - 1] + dungeon[0][c]
    health = 0

    for r in range(1, row):
        for c in range(1, col):
            dp[r][c] = max(dp[r - 1][c], dp[r][c - 1]) + dungeon[r][c]
            health = min(health, dp[r][c])
    print(dp)
    return abs(health) + 1


print(calculateMinimumHP([
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]))
