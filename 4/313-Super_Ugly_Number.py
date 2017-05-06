# coding=utf-8
'''
跟ugly number II类似，。这道题给了primes而不是2,3,5.定义一个跟primes一样长的，存储对应prime的下标。
每次遍历下标，找到在res中下标对应的的数与primes中下标对应的数相乘。找到最小的，添加到res中，并查看最小数对应的下标，
把这个下标加1。dp问题
'''
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        idx = [0 for _ in range(len(primes))]
        res = [1]
        cnt = 0
        while cnt < n:
            min_buf = []
            for i in range(len(idx)):
                min_buf.append(res[idx[i]] * primes[i])
            min_buf = min(min_buf)
            res.append(min_buf)
            for i in range(len(idx)):
                if res[idx[i]] * primes[i] == min_buf:
                    idx[i] += 1
            cnt += 1
        return res[n-1]


solution = Solution()
print(solution.nthSuperUglyNumber(12, [2, 7, 13, 19]))
