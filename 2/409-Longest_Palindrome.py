'''
偶数个字符可以组成回文，奇数个的字符只有个数-1个可以组成回文。
回文里面只允许一个奇数字符存在
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}
        for v in s:
            hash_map[v] = hash_map.get(v, 0) + 1
        res = 0
        flag = 0
        for v in hash_map.values():
            if v % 2 == 0:
                res += v
            else:
                flag = 1
                res += v - 1
                
        return res + flag