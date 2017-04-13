# coding=utf-8
'''
用两个哈希表，存储每个字母的下标，对比下标是否一样
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table = {}
        for i in range(len(s)):
            if table.get(s[i], "Null") == "Null":
                table[s[i]] = []
            table[s[i]].append(i)
        t_table = {}
        for i in range(len(t)):
            if t_table.get(t[i], "Null") == "Null":
                t_table[t[i]] = []
            t_table[t[i]].append(i)
        for i in range(len(s)):
            if table[s[i]] != t_table[t[i]]:
                return False
        return True