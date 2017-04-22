# coding=utf-8
'''
先找到到n在第几个数里面，再找在这个数的第几位
'''
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        i = 1
        while n > 9 * 10 ** (i - 1) * i:
            n -= 9 * (10 ** (i - 1)) * i
            i += 1
        if n % i == 0:
            num = n / i - 1
        else:
            num = n / i

        thisnum = 10 ** (i - 1) + num
        bit = (n - 1) % i
        return int(str(thisnum)[bit])



solution = Solution()
print(solution.findNthDigit(10))
