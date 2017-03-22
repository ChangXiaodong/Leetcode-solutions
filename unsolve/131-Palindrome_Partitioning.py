class Solution(object):
    def dfs(self, index, s, path, ret):
        if

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        if n <= 0:
            return []
        res = []
        for i in range(n):
            for j in range(n - 1, i, -1):
                a = s[i:j]
                if a == a[::-1]:
                    buf = []
                    if s[:i]:
                        buf.append(s[:i])
                    if a:
                        buf.append(a)
                    res.append(buf)

        return res


solution = Solution()
print(solution.partition("aab"))
