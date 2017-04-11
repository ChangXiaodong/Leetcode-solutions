class Solution(object):
    def dfs(self, board, word, row, col, visited):
        if not word:
            return True
        rows = board.__len__()
        cols = board[0].__len__()
        if row < 0 or row >= rows:
            return False
        if col < 0 or col >= cols:
            return False
        if visited[row][col]:
            return False
        if word[0] != board[row][col]:
            return False
        visited[row][col] = True

        if self.dfs(board, word[1:], row + 1, col, visited):
            return True
        if self.dfs(board, word[1:], row, col + 1, visited):
            return True
        if self.dfs(board, word[1:], row - 1, col, visited):
            return True
        if self.dfs(board, word[1:], row, col - 1, visited):
            return True

        visited[row][col] = False
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        if not word:
            return True
        rows = board.__len__()
        cols = board[0].__len__()

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, word, i, j, visited):
                    return True
        return False


solution = Solution()
print(solution.exist(["ABCE","SFCS","ADEE"],"ABCCED"))