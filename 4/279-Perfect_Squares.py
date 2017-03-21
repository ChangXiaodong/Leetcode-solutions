'''
方法1：dp  662ms
dp[i] = min(dp[i], dp[i - j ** 2] + 1)  for j in range(1, j ** 2 < i)

方法2：dp 546ms

方法3：数学计算法 375ms
'''


class Solution(object):
    # dp
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1
        return dp[-1]

    def numSquares1(self, n):
        if n <= 0:
            return 0
        dp = [0]
        while dp.__len__() <= n:
            buf = float("inf")
            m = dp.__len__()
            j = 1
            while j ** 2 <= m:
                buf = min(buf, dp[m - j ** 2] + 1)
                j += 1
            dp.append(buf)
        return dp[-1]

    def is_square(self, n):
        sqrt_n = int(n ** 0.5)
        return sqrt_n ** 2 == n

    def numSquares2(self, n):
        if self.is_square(n):
            return 1
        while n & 3 == 0:
            n = n >> 2
        if n & 7 == 7:
            return 4
        sqrt_n = int(n ** 0.5)
        for i in range(1, sqrt_n + 1):
            if self.is_square(n - i ** 2):
                return 2
        return 3


solution = Solution()
print(solution.numSquares2(7))
