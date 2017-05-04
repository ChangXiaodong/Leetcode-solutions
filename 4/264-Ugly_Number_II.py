'''
We have an array k of first n ugly number. We only know, at the beginning, the first one, which is 1. Then

k[1] = min( k[0]x2, k[0]x3, k[0]x5). The answer is k[0]x2. So we move 2's pointer to 1. Then we test:

k[2] = min( k[1]x2, k[0]x3, k[0]x5). And so on. Be careful about the cases such as 6, in which we need to forward both pointers of 2 and 3.

x here is multiplication.
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j, k = 0, 0, 0
        res = [1]
        cnt = 1
        while cnt < n:
            min_buf = min([res[i]*2, res[j]*3, res[k]*5])
            if min_buf == res[i]*2:
                i += 1
            if min_buf == res[j]*3:
                j += 1
            if min_buf == res[k]*5:
                k += 1
            res.append(min_buf)
            cnt += 1
        return res[n-1]


solution = Solution()
print(solution.nthUglyNumber(10))
