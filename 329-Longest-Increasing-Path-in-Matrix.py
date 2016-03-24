def dfs(x,y,x_range, y_range,m):
    if m[x][y]:
        val = m[x][y]
        length = 1 + max(
            dfs(x+1, y,x_range,y_range,m) if x+1<x_range and val > m[x+1][y] else 0,
            dfs(x, y+1,x_range,y_range,m) if y+1<y_range and val > m[x][y+1] else 0,
            dfs(x-1, y,x_range,y_range,m) if x and val > m[x-1][y] else 0,
            dfs(x, y-1,x_range,y_range,m) if y and val > m[x][y-1] else 0
        )
        return length
    else:
        return 0

def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    y_range = len(matrix[0])
    x_range = len(matrix)
    max = 0
    coordinate = []
    length = []
    for i in range(x_range):
        for j in range(y_range):
            if matrix[i][j]>max:
                coordinate = []
                max = matrix[i][j]
                coordinate.append([i,j])
            if matrix[i][j] == max:
                coordinate.append([i,j])
    for i,j in coordinate:
        length.append(dfs(i,j,x_range,y_range,matrix))
    length.sort()
    return length[-1]

def longestIncreasingPath1(matrix):
    def dfs(i, j):

        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]: return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return max(dfs(x, y) for x in range(M) for y in range(N))

# print longestIncreasingPath1(
# [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
# )
print longestIncreasingPath(
    [
        [1,1,1],
        [1,1,1]
    ]
)

