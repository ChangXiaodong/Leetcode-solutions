'''
判断给定的矩阵是不是符合数独要求，要求有三条:
1.每一行只包含1-9，每个数字只出现一次
2.每一列只包含1-9，每个数字只出现一次
3.每3*3的矩阵内只包含1-9，只出现一次。3*3的矩阵没有重叠

方法：先检测每行是不是符合要求，在检查每列是不是符合要求
最后检查3*3内是不是符合要求
'''

class Solution(object):
    def valid_row(self, board):
        for i in range(9):
            buf = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in buf:
                        return False
                    elif int(board[i][j]) > 9 or int(board[i][j]) < 0:
                        return False
                    else:
                        buf.append(board[i][j])
        return True

    def valid_col(self, board):
        for j in range(9):
            buf = []
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in buf:
                        return False
                    elif int(board[i][j]) > 9 or int(board[i][j]) < 0:
                        return False
                    else:
                        buf.append(board[i][j])
        return True

    def valid_grid(self, board, r, c):
        buf = []
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if board[i][j] != ".":
                    if board[i][j] in buf:
                        return False
                    elif int(board[i][j]) > 9 or int(board[i][j]) < 0:
                        return False
                    else:
                        buf.append(board[i][j])
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False
        if not self.valid_row(board):
            return False
        if not self.valid_col(board):
            return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.valid_grid(board, i, j):
                    return False
        return True
