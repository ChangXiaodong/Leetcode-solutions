class Solution(object):
    def help(self, matrix, res):
        if not matrix:
            return res
        row = matrix.__len__()
        col = matrix[0].__len__()
        if row * col == 0:
            return res
        for i in range(col):
            res.append(matrix[0][i])
        for i in range(1, row):
            res.append(matrix[i][-1])
        if col >= 2 and row >= 2:
            for i in range(col - 2, -1, -1):
                res.append(matrix[-1][i])
        if row >= 3 and col >= 2:
            for i in range(row - 2, 0, -1):
                res.append(matrix[i][0])
        if col >= 2 and row >= 3:
            next_matrix = []
            for r in range(1, row - 1):
                next_matrix.append(matrix[r][1:col - 1])
            self.help(next_matrix, res)
        else:
            return res

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        self.help(matrix, res)
        return res


solution = Solution()
print(solution.spiralOrder([[2,3]]))
