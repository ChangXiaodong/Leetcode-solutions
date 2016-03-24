def LCS_length(X, Y):
    m = len(X)
    n = len(Y)
    b = [["" for i in range(n + 1)] for i in range(m + 1)]
    c = [[0 for i in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = '\\'
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = '|'
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = '-'
    print_LCS(b, X, m, n)
    return c, b


def print_LCS(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == '\\':
        print X[i - 1]
        print_LCS(b, X, i - 1, j - 1)
    elif b[i][j] == '|':
        print_LCS(b, X, i - 1, j)
    else:
        print_LCS(b, X, i, j - 1)


def get_LCS_length(X, Y, c, i, j):
    if c[i][j] > 0:
        return c[i][j]
    if i == 0 or j == 0:
        return 0
    if X[i - 1] == Y[j - 1]:
        c[i][j] = get_LCS_length(X, Y, c, i - 1, j - 1)
    else:
        c[i][j] = max(get_LCS_length(X, Y, c, i - 1, j), get_LCS_length(X, Y, c, i, j - 1))
    return c[i][j]


def memorized_LCS_length(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for i in range(n + 1)] for i in range(m + 1)]
    get_LCS_length(X, Y, c, m, n)
    print c


c, b = LCS_length(['A', 'B', 'C', 'B', 'D', 'A', 'B'], ['B', 'D', 'C', 'A', 'B', 'A'])
for line in c:
    print line
for line in b:
    print line

print memorized_LCS_length(['A', 'B', 'C', 'B', 'D', 'A', 'B'], ['B', 'D', 'C', 'A', 'B', 'A'])
