def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    length = len(triangle)
    triangle_steps = [[] for i in range(length)]

    for row in range(length, 0, -1):
        if row < length:
            for i, v in enumerate(triangle[row - 1]):
                triangle_steps[row - 1].append(v + min(triangle_steps[row][i], triangle_steps[row][i + 1]))
        else:
            triangle_steps[row - 1] = triangle[row - 1]
    return triangle_steps[0][0]

def minimumTotal1(triangle):
    if not triangle:
        return
    res = [[0 for i in range(len(row))] for row in triangle]
    res[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                res[i][j] = res[i-1][j] + triangle[i][j]
            elif j == len(triangle[i])-1:
                res[i][j] = res[i-1][j-1] + triangle[i][j]
            else:
                res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
    return min(res[-1])


print(minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))

print(minimumTotal1([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
