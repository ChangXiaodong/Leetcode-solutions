def order_matrix_chain(p):
    n = len(p)
    m = [[0 for i in range(n)] for i in range(n)]
    s = [[0 for i in range(n)] for i in range(n)]
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')  # max infinite
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    print print_optimal_paren(s, 1, 6)
    return m, s


def print_optimal_paren(s, i, j):
    if i == j:
        return i
    else:
        return print_optimal_paren(s, i, s[i][j]), print_optimal_paren(s, s[i][j] + 1, j)


def loopup_chain(m, s, p, i, j):
    if m[i][j] < float('inf'):
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = loopup_chain(m, s, p, i, k) + loopup_chain(m, s, p, k + 1, j) + p[i - 1] * p[k] * p[j]
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k
    return m[i][j]


def memoized_matrix_chain(p):
    n = len(p)
    m = [[float('inf') for i in range(n)] for i in range(n)]
    s = [[0 for i in range(n)] for i in range(n)]
    loopup_chain(m, s, p, 1, 6)
    return m, s


print order_matrix_chain([30, 35, 15, 5, 10, 20, 25])
print memoized_matrix_chain([30, 35, 15, 5, 10, 20, 25])
