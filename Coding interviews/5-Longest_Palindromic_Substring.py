#http://articles.leetcode.com/longest-palindromic-substring-part-ii/
#https://leetcode.com/articles/longest-palindromic-substring/
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
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
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
    return s[(index - 1 - max_len) / 2:max_len]



print(longestPalindrome("babcbabcbaccba"))
