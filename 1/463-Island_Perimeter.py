class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row_num = grid.__len__()
        col_num = grid[0].__len__()
        res = 0
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == 1:
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        res += 1
                    if i + 1 >= row_num or grid[i + 1][j] == 0:
                        res += 1
                    if j - 1 < 0 or grid[i][j-1] == 0:
                        res += 1
                    if j + 1 >= col_num or grid[i][j+1] == 0:
                        res += 1
        return res