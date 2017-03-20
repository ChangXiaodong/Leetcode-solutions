'''
方法1：用哈希表
方法2：异或
'''
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash_map = {}
        for v in s:
            hash_map[v] = hash_map.get(v, 0) + 1
        for v in t:
            if hash_map.get(v, "Null") == "Null" or hash_map.get(v, "Null") == 0:
                return v
            hash_map[v] -= 1

    def findTheDifference1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for v in s:
            res = res ^ ord(v)
        for v in t:
            res = res ^ ord(v)
        return chr(res)
