#coding=utf-8
'''
dp[n] = Ture if dp[i] == True and dp[i+1:n] == True
'''


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    n = len(s) + 1
    dp = [False for _ in range(n)]
    dp[0] = True
    for i in range(1, n):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[len(s)]

print(wordBreak("aaaaaaa", ["aaaa", "aaa"]))
