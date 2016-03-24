def optimal_bst(p, q, n):
    e = [[0 for i in range(n + 1)] for i in range(n + 2)]
    w = [[0 for i in range(n + 1)] for i in range(n + 2)]
    root = [[0 for i in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]
    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i][j] = float('inf')
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return e, root


e, root = optimal_bst([0, 0.15, 0.1, 0.05, 0.1, 0.2], [0.05, 0.1, 0.05, 0.05, 0.05, 0.1], 5)
for l in e:
    print l
for l in root:
    print l
