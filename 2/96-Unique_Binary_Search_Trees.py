#coding=utf-8
'''
从1到n遍历, 把该数字当做根节点，看剩下的数字组成的BST有多少种组合形式。
dp[n] = dp[0]*dp[n-1] + dp[1]*dp[n-2] + dp[2]*dp[n-3] + .... + dp[n-3]*dp[2] + dp[n-2]*dp[1] + dp[n-1]*dp[0]
1,2,3,4,5
root = 1:左子树为空，    右子树为2,3,4,5   res+= dp[0]*dp[4]
root = 2:左子树为1，     右子树为3,4,5     res+= dp[1]*dp[3]
root = 3:左子树为1,2     右子树为4,5       res+= dp[2]*dp[2]
root = 4:左子树为1,2,3   右子树为5         res+=dp[3]*dp[1]
root = 5:左子树为1,2,3,4 右子树为空        res+=dp[4]*dp[0]
'''
def numTrees(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 5
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 5
    for j in range(4,n + 1):
        res = 0
        for i in range(j):
            left = dp[i]
            right = dp[j - 1 - i]
            res += left * right
            if i == j - 1:
                dp[j] = res
    res = 0
    for i in range(n):
        left = dp[i]
        right = dp[n - 1 - i]
        res += left * right
    return res


print(numTrees(5))
