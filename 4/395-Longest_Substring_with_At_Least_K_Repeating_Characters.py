'''
统计s内每个字符出现的次数，如果某个字母出现的次数小于k，那么这个字符不可能在最长子字符中，以这个字符为分割线，查找分割出的最长子字符串
'''

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for v in set(s):
            if s.count(v) < k:
                return max(self.longestSubstring(t, k) for t in s.split(v))
        return len(s)
