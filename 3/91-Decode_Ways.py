'''
1）若第n个字符在1到9之间，则n长度的字符串能够解释的数目包含n-1长度字符串能够解释的数目。
2）若第n-1个字符与第n个字符可以解释为一个字母时，则n长度的字符串能够解释的数目包含n-2长度字符串能够解释的数目。
'''

def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    n = len(s)
    if s[0] == '0':
        return 0
    r1 = 1
    r2 = 1
    for i in range(1, n):
        if s[i] == '0':
            r1 = 0
        if s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6':
            r1 = r1 + r2
            r2 = r1 - r2
        else:
            r2 = r1
    return r1

def numDecodings1(s):
    if not s:
        return 0
    n = len(s)
    if s[0] == '0':
        return 0
    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 2 if s[0] == '1' or s[0] == '2' and s[1] <= '6' else 1
    for i in range(2, n):
        if s[i] != '0':
            dp[i] = dp[i - 1]
        if s[i - 1] != '0' and s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6':
            dp[i] += dp[i - 2]
    return dp[-1]


print(numDecodings('6110111'))
print(numDecodings1('6110111'))
