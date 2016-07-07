def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for i in range(n+1)] for j in range(n+1)]
    s = [[0 for i in range(n+1)] for j in range(n+1)]
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


def print_matrix_order(s, i, j):
    if i == j:
        print("A" + str(i))
    else:
        print("(")
        print_matrix_order(s, i, s[i][j])
        print_matrix_order(s, s[i][j] + 1, j)
        print(")")


if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    m, s = matrix_chain_order(p)
    print(m)
    print_matrix_order(s, 1, 6)