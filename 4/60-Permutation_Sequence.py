class Solution(object):
    def dfs(self, n, buf, k, used):
        if len(buf) == n:
            if self.kth == k:
                self.res = buf[:]
                return True
            self.kth += 1
            return False
        for i in range(1, n+1):
            if used[i] == False:
                used[i] = True
                buf.append(i)
                if self.dfs(n, buf, k, used):
                    return True
                buf.pop()
                used[i] = False
        return False
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.res = []
        self.kth = 1
        used = [False for _ in range(n+1)]
        self.dfs(n, [], k, used)
        return "".join(map(str, self.res))


s = Solution()
print(s.getPermutation(9, 171669))
