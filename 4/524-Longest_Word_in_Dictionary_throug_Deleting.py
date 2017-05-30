# coding=utf-8
'''
双指针题，查找思想如下：
1.先对d中的单次按照长度和字典顺序排序，先查找最长，字典顺序最低的单词。
2.删除时在s中使用一个指针p1，在被查找的单词中使用一个指针p2。
3.当字母相同时p2和p1同时加1，否则只把p1加1.
4.当p2长度和被查找单次相同时，则查找成功。返回该单次
'''

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        length_table = {}
        for word in d:
            word_len = len(word)
            if length_table.get(word_len, "null") == "null":
                length_table[word_len] = []
            length_table[word_len].append(word)
        dec_order = sorted(length_table.keys())
        res = []
        while dec_order:
            for w in length_table[dec_order.pop()]:
                p1 = 0
                p2 = 0
                while p1 < len(s) and p2 < len(w):
                    if s[p1] == w[p2]:
                        p2 += 1
                    p1 += 1
                if p2 == len(w):
                    res.append(w)
            if res:
                return sorted(res)[0]
        return ""

    def findLongestWord1(self, S, D):
        D.sort(key=lambda x: (-len(x), x))
        for word in D:
            i = 0
            for c in S:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""


s = Solution()
print(s.findLongestWord("bab", ["ba", "ab", "a", "b"]))
