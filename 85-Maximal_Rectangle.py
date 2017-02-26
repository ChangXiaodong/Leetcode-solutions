def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
        return 0
    row = matrix.__len__()
    col = matrix[0].__len__()
    left = [0] * col
    right = [col] * col
    height = [0] * col
    area = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '1':
                height[j] += 1
            else:
                height[j] = 0
        cur_left = 0
        for j in range(col):
            if matrix[i][j] == '1':
                left[j] = max(left[j], cur_left)
            else:
                left[j] = 0
                cur_left = j + 1
        cur_right = col
        for j in range(col - 1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], cur_right)
            else:
                right[j] = col
                cur_right = j

        for j in range(col):
            area = max(area, (right[j] - left[j]) * height[j])

    return area


print(maximalRectangle([
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0]
]))
