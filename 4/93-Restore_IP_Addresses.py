# coding=utf-8
'''
注意0开头的地址，注意ip长度只能有四段
'''
class Solution(object):
    def dfs(self, s, buf):
        if not s:
            for v in buf:
                if len(v) > 1 and v[0] == '0':
                    return
                if int(v) > 255:
                    return

            if buf.__len__() != 4:
                return
            ans = ".".join(buf)
            if ans not in self.res:
                self.res.append(ans)
            return
        for i in range(len(s)):
            if s[:i+1] and int(s[:i+1]) <= 255:
                if buf.__len__() < 3:
                    buf.append(s[:i+1])
                    self.dfs(s[i+1:], buf)
                else:
                    buf.append(s)
                    self.dfs('', buf)
                buf.pop()


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        self.res = []
        self.dfs(s, [])
        return self.res
solution = Solution()
print(solution.restoreIpAddresses("010010"))
