'''
这里用了一个缓存矩阵，计算完后把缓存矩阵赋给原矩阵
如果一定要是inplace，就在一个店内存字符串
"00"代表这一轮是0，下一轮是0
"01"代表这一轮是0，下一轮是1
如此类推
'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board:
            return
        row = board.__len__()
        col = board[0].__len__()
        res = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                live_count = 0
                if i - 1 >= 0 and board[i - 1][j] == 1:
                    live_count += 1
                if j + 1 < col and board[i][j + 1] == 1:
                    live_count += 1
                if i + 1 < row and board[i + 1][j] == 1:
                    live_count += 1
                if j - 1 >= 0 and board[i][j - 1] == 1:
                    live_count += 1
                if i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == 1:
                    live_count += 1
                if i + 1 < row and j - 1 >= 0 and board[i + 1][j - 1] == 1:
                    live_count += 1
                if i - 1 >= 0 and j + 1 < col and board[i - 1][j + 1] == 1:
                    live_count += 1
                if i + 1 < row and j + 1 < col and board[i + 1][j + 1] == 1:
                    live_count += 1
                if board[i][j] == 1:
                    if live_count < 2:
                        res[i][j] = 0
                    elif live_count == 2 or live_count == 3:
                        res[i][j] = 1
                    elif live_count > 3:
                        res[i][j] = 0
                else:
                    if live_count == 3:
                        res[i][j] = 1
        board[:] = res[:]


solution = Solution()
print(solution.gameOfLife([[1, 1]]))

