# http://articles.leetcode.com/longest-palindromic-substring-part-ii/
# https://leetcode.com/articles/longest-palindromic-substring/
def preProcess(s):
    new_s = '#'
    for m in s:
        new_s += m + '#'
    return new_s


def longestPalindrome(s):
    T = preProcess(s)
    n = len(T)
    P = [0 for _ in range(n)]
    C = 0
    R = 0
    for i in range(1, n - 1):
        i_mirror = 2 * C - i
        if R > i:
            P[i] = min(R - i, P[i_mirror])
        else:
            P[i] = 0
        while i + 1 + P[i] < n and T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1
        if i + P[i] > R:
            C = i
            R = i + P[i]

    max_len = 0
    index = 0
    for i, v in enumerate(P):
        if P[i] > max_len:
            max_len = P[i]
            index = i
    return T[index - max_len:index + max_len].replace("#", "")


def isPalindrome(s):
    pass


def dfs(i, j, s, P):
    P[i][j] = P[i + 1][j - 1] and s[i] == s[j]


def longestPalindrome_dynamic(s):
    if not s:
        return ''
    if s.__len__() == 1:
        return s
    length = len(s)
    P = [[False for _ in range(length)] for _ in range(length)]
    for i in range(length):
        P[i][i] = True
    max_len = 1
    index = 0
    for i in range(length - 1):
        if s[i] == s[i + 1]:
            P[i][i + 1] = True
            max_len = 2
            index = i
    for n in range(2, length + 1):
        for i in range(length - n + 1):
            j = i + n - 1
            if s[i] == s[j] and P[i + 1][j - 1]:
                P[i][j] = True
                max_len = n
                index = i

    return s[index:index+max_len]


print(longestPalindrome("aaaa"))
print(longestPalindrome_dynamic("abcda"))
