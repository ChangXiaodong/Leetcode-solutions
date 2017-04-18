# coding=utf-8
'''
注意最后有一个或多个空格的情况
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        while s and s[-1] == " ":
            s = s[:-1]
        words = s.split(" ")
        return len(words[-1])
