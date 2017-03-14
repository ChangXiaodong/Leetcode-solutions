def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    row_num = matrix.__len__()
    col_num = matrix.__len__()
    i = 0
    while i < row_num - 1:
        if matrix[i][-1] < matrix[i + 1][0]:
            if k <= col_num:
                return matrix[i][k - 1]
            k -= col_num
            i += 1
        else:
            matrix[i][-1], matrix[i + 1][0] = matrix[i + 1][0], matrix[i][-1]
            for j in range(col_num - 1):
                if matrix[i + 1][j] > matrix[i + 1][j + 1]:
                    matrix[i + 1][j], matrix[i + 1][j + 1] = matrix[i + 1][j + 1], matrix[i + 1][j]
    return matrix[i][k - 1]



print(kthSmallest([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
