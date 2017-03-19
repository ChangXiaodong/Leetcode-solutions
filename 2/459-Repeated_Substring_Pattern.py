# coding=utf-8
'''
方法1：子字符串长度为1到n/2，假设i为当前遍历长度，若s除前i个字符剩下的字符为copy_s,对比s的前i个字符和copy_s的前i个字符，
若想等，删除copy_s的前i个字符。若能够将copy_s全部删空，返回True

方法2：基本原理，（虽然我也不知道为啥，可能是因为某种对称性）
要检查的字符串为s
ss = s + s
若ss去掉第一个和最后一个字符ss[1:-1]包含s，返回True，否则返回False
'''
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        n = len(s)

        for i in range(1, n/2 + 1):
            copy_s = s[i:]
            basic = s[:i]
            while len(copy_s) >= i:
                if basic == copy_s[:i]:
                    copy_s = copy_s[i:]
                else:
                    break
            if not copy_s:
                return True
        return False

    def repeatedSubstringPattern1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        ss = (s + s)[1:-1]
        return s in ss


solution = Solution()
print(solution.repeatedSubstringPattern("abababaaba"))
