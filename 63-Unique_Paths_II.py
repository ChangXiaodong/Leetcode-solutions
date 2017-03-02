def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if not obstacleGrid:
        return 0
    row = obstacleGrid.__len__()
    col = obstacleGrid[0].__len__()

    if row * col == 0:
        return 0

    if obstacleGrid[0][0] == 1:
        return 0

    if row == 1:
        if 1 in obstacleGrid[0]:
            return 0
        else:
            return 1
    if col == 1:
        for r in obstacleGrid:
            for v in r:
                if v == 1:
                    return 0
        return 1
    dp = [[0 for _ in range(col)] for _ in range(row)]
    for r in range(row):
        if obstacleGrid[r][0] != 1:
            dp[r][0] = 1
        else:
            break

    for c in range(col):
        if obstacleGrid[0][c] != 1:
            dp[0][c] = 1
        else:
            break

    dp[0][0] = 0
    for r in range(1, row):
        for c in range(1, col):
            if obstacleGrid[r][c] != 1:
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
            else:
                dp[r][c] = 0
    return dp[row - 1][col - 1]


print(uniquePathsWithObstacles([
    [0, 0],
    [1, 1],
    [0, 0]
]))
