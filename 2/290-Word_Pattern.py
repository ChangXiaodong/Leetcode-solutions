# coding=utf-8
'''
建两个哈希表相互保存映射
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        if len(pattern) != len(words):
            return False
        table = {}
        words_table = {}

        n = len(pattern)
        for i in range(n):
            if table.get(pattern[i], "Null") != "Null":
                if table[pattern[i]] != words[i]:
                    return False
            else:
                if words_table.get(words[i], "Null") != "Null":
                    if words_table[words[i]] != pattern[i]:
                        return False
                else:
                    words_table[words[i]] = pattern[i]
                table[pattern[i]] = words[i]
        return True

