def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    n = len(s)
    dp = [0 for _ in range(n)]
    if s[0] == '0':
        return 0
    else:
        dp[0] = 1
    for i in range(1, n):

    return dp[n - 1]


print(numDecodings('110'))
