'''
方法1：给每个字符串排序，当作key，value存排序前的。若果key已经存在，就把该字符串添加在已经存在value里面
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        hash_map = {}
        for s in strs:
            key = ""
            for c in sorted(s):
                key += c
            if hash_map.get(key, 0) == 0:
                hash_map[key] = [s]
            else:
                hash_map[key].append(s)
        res = []
        for key in hash_map.keys():
            res.append(hash_map[key])
        return res

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
