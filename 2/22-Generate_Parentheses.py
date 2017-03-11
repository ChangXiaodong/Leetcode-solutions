def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n <= 0:
        return ""
    dp = {1: ["()"], 2: ["()()", "(())"]}
    if n <= 2:
        return dp[n]
    for i in range(3, n + 1):
        dp[i] = []
        for par in dp[i - 1]:
            for index in range(len(par)):
                s = par[:index] + "()" + par[index:]
                if s not in dp[i]:
                    dp[i].append(s)
    return dp[n]


print(generateParenthesis(4))
