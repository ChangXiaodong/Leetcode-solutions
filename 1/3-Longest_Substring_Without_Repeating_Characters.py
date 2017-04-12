class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        string = ""
        length = 0
        max_len = 0
        for i in range(len(s)):
            if not s[i] in string:
                string += s[i]
                length += 1
            else:
                max_len = max(length, max_len)
                index = string.index(s[i]) + 1
                string = string[index:] + s[i]
                length = len(string)
        return max(max_len, length)

    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        string = {}
        max_len = 0
        j = 0
        i = 0
        while i < len(s):
            if string.get(ord(s[i]), "Null") == "Null":
                string[ord(s[i])] = i
                max_len = max(string.keys().__len__(), max_len)
                i += 1
            else:
                string.pop(ord(s[j]))
                j += 1
        return max_len

solution = Solution()
print(solution.lengthOfLongestSubstring1("abcabcbb"))
