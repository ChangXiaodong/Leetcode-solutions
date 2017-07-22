class Solution(object):
    def bt(self, board, nums):
        pass

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        nums = [i for i in range(1, 10)]
        rows = len(board)
        cols = len(board[0])
        dp = [[[] for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ".":
                    nums = [x for x in range(1, 10)]
                    m = i / 3 * 3
                    n = j / 3 * 3
                    for a in range(3):
                        for b in range(3):
                            if board[m+a][n+b] != '.':
                                nums.remove(int(board[m + a][n + b]))
                    for col in range(cols):
                        if board[i][col] != '.' and int(board[i][col]) in nums:
                            nums.remove(int(board[i][col]))
                    for row in range(rows):
                        if board[row][j] != '.' and int(board[row][j]) in nums:
                            nums.remove(int(board[row][j]))
                    dp[i][j] = nums



solution = Solution()
print(solution.solveSudoku(
    ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5",
     "....8..79"]))
