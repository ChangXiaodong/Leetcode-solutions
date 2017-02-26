# coding=utf-8
'''
dp[i][j] 代表字符串s从i到j最大回文长度
if s[i] == s[j] and dp[i+1][j-1]:
    dp[i][j] += 2
else:
    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

'''


def longestPalindromeSubseq(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    if s == s[::-1]:
        return len(s)
    n = len(s)
    dp = [[0 for __ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in reversed(range(n - 1)):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]


def longestPalindromeSubseq1(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    dp = [1] * n
    for i in range(1, n):
        pre = dp[i]
        for j in reversed(range(i)):
            tmp = dp[j]
            if s[j] == s[i]:
                dp[j] = 2 + pre if j + 1 <= i - 1 else 2
            else:
                dp[j] = max(dp[j + 1], dp[j])
            pre = tmp
    return dp[0]


print(longestPalindromeSubseq1('bbbab'))
