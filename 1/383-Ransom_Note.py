'''
题目意思是：magazine中的字母可以可以构成ransomNote， 每个字母只能用一次。
统计字母个数即可
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash_map = {}
        for s in magazine:
            hash_map[s] = hash_map.get(s, 0) + 1
        for s in ransomNote:
            if hash_map.get(s, 0) != 0:
                hash_map[s] -= 1
            else:
                return False
        return True
