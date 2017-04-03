'''
注意条件要求。
题目要求，如果s长度小于k，翻转所有字符串。
否则翻船第奇数k个字符串。
'''

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s:
            return s
        n = len(s)
        if n < k:
            return s[::-1]
        i = 0
        string = ""
        while i < n:
            string += s[i:i + k][::-1]
            i += k
            left = n - i
            if left < k:
                string += s[i:]
                break
            elif k < left < 2 * k:
                string += s[i:i + k]
                i += k
                string += s[i:][::-1]
                break
            string += s[i:i + k]
            i += k
        return string