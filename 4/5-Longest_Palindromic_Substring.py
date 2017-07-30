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




class Solution(object):
    def lcs(self, s1, s2):
        dp = [[0 for _ in range(len(s1))] for _ in range(len(s2))]
        res = ''
        max_len = -1
        x = 0
        y = 0
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    x = i
                    y = j
        while x >= 0 and y >= 0:
            if s1[x] != s2[y] or max_len <= 0:
                break
            res += s1[x]
            x -= 1
            y -= 1
            max_len -= 1
        return res[::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = ''
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j] and (not res or j - i + 1 > len(res)):
                    res = s[i:j + 1]
        return res



# print(longestPalindrome("aaaa"))
# print(longestPalindrome_dynamic("abcda"))
s = Solution()
print(s.longestPalindrome("abcdasdfghjkldcba"))
