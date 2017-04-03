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

solution = Solution()
print(solution.partition("aabbaabbaa"))


