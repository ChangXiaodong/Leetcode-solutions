class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = grid.__len__()
        col = grid[0].__len__()
        table = [[] for _ in range(row)]
        for r in range(row):
            start_index = col + 1
            end_index = col + 1
            for c in range(col):
                if grid[r][c] == '1':
                    start_index = min(c, start_index)
                else:
                    if start_index < col:
                        end_index = min(end_index, c-1)
                if start_index < col and end_index < col + 1:
                    table[r].append([start_index, end_index])
                    start_index = col + 1
                    end_index = col + 1
        number = 1 if '1' in grid else 0
        for r in range(1, row):
            for item in table[r]:
                for last_item in table[r-1]:
                    if item[0] > last_item[1] or item[1] < last_item[0]:
                        number += 1
        return number

solution = Solution()
print(solution.numIslands(["11000","11000","00100","00011"]))