class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        valid = lambda x: x == x[::-1]
        n = len(s)
        if n <= 0:
            return []
        ans = []

        def dfs(index, res):
            if index >= n:
                ans.append(res)
                return
            for j in range(index + 1, n + 1):
                if valid(s[index:j]):
                    dfs(j, res + [s[index:j]])

        dfs(0, [])
        return ans

class Solution2(object):
    def dfs(self, s, buf, res):
        if not s:
            res.append(buf[:])
            return
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                buf.append(s[:i])
                self.dfs(s[i:], buf, res)
                buf.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        res = []
        self.dfs(s, [], res)
        return res

solution = Solution2()
print(solution.partition("aab"))


