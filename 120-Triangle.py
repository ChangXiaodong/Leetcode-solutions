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
    return triangle_steps


minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
])
