# coding=utf-8
'''
minWindow类问题
http://www.rudy-yuan.net/archives/185/
首先将要匹配的字符串p转化为哈希表
定义两个指针left，right。当right在哈希表中，并且对应计数大于0，则说明right是p的子字符串。cnt + 1.
当cnt等于p长度时，说明字符串匹配完毕，将left加入到res中
right-left的长度应当等于p的长度。当right右移时，left也右移。并且把left左边刚移出的字符还原统计，即更新cnt和对应哈希表内的值
'''
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        table = {}
        for v in p:
            table[v] = table.get(v, 0) + 1
        cnt = 0
        left, right = 0, 0
        res = []
        n = len(p)
        while right < len(s):
            if table.get(s[right], "Null") != "Null":
                table[s[right]] -= 1
                if table[s[right]] >= 0:
                    cnt += 1
            if cnt == n:
                res.append(left)
            right += 1
            if right - left >= n:
                if table.get(s[left], "Null") != "Null":
                    table[s[left]] += 1
                    if table[s[left]] > 0:
                        cnt -= 1
                left += 1

        return res

solution = Solution()
print(solution.findAnagrams("abab" ,"ab"))
