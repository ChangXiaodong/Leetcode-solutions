'''
主要注意区分矩阵中自带的原始的0，和后期变的0.后期变的0不继续做变换。
'''
class Solution(object):
    def set(self, matrix, i, j):
        row = matrix.__len__()
        col = matrix[0].__len__()
        for c in range(col):
            if matrix[i][c] == 0:
                break
            matrix[i][c] = "0"
        for r in range(row):
            if matrix[r][j] == 0:
                break
            matrix[r][j] = "0"

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row = matrix.__len__()
        col = matrix[0].__len__()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[i][j] = "0"
                    self.set(matrix, i, j)
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0