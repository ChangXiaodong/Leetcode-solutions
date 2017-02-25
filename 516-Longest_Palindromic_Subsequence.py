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
    n = len(s)
    dp = [1 for _ in range(n)]
    for i in range(n - 1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                if j > i + 1:
                    dp[j] += 2
                else:
                    dp[j] = 2
            else:
                dp[j] = max(dp[j], dp[j - 1])
    return dp

def longestPalindromeSubseq1(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    dp = [1] * n
    for j in xrange(1, len(s)):
        pre = dp[j]
        for i in reversed(xrange(0, j)):
            tmp = dp[i]
            if s[i] == s[j]:
                dp[i] = 2 + pre if i + 1 <= j - 1 else 2
            else:
                dp[i] = max(dp[i + 1], dp[i])
            pre = tmp
    return dp[0]

print(longestPalindromeSubseq1('ddddd'))
