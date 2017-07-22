class Solution(object):
    def dfs(self, matrix, access, res, steps, i, j):
        if i >= len(matrix) or j >= len(matrix[0]) or access[i][j] or matrix[i][j] == 0:
            return steps
        access[i][j] = True
        res = min(self.dfs(matrix, access, res, steps + 1, i + 1, j), res)
        res = min(self.dfs(matrix, access, res, steps + 1, i - 1, j), res)
        res = min(self.dfs(matrix, access, res, steps + 1, i, j + 1), res)
        res = min(self.dfs(matrix, access, res, steps + 1, i, j - 1), res)
        access[i][j] = False
        return res

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        access = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != 0:
                    matrix[i][j] = self.dfs(matrix, access, float("inf"), 0, i, j)
        return matrix


solution = Solution()
print(solution.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
