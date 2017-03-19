# coding=utf-8
'''
从第一个元素开始遍历，如果这个元素为1，则landnum加一。递归的搜索这个元素的上下左右，如果为1则置为0。
然后遍历下一个元素。
'''
class Solution(object):
    def dfs(self, grid, i, j):
        if not grid:
            return
        if i< 0 or i >= grid.__len__() or j < 0 or j >= grid[0].__len__():
            return
        if grid[i][j] == "1":
            grid[i][j] = 0
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i, j - 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = grid.__len__()
        col = grid[0].__len__()
        num = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    num += 1
                    self.dfs(grid, i, j)
        return num