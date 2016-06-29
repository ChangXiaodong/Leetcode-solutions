__author__ = 'Changxiaodong'
'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

Beware of overflow.
'''
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        q, x, ans = n, 1, 0
        while q > 0:
            digit = q % 10
            q /= 10
            ans += q * x
            if digit == 1:
                ans += n % x + 1
            elif digit > 1:
                ans += x
            x *= 10
        return ans

    def countDigitOne1(self,k):
        count = 0
        factor = 1
        n = k
        while(n>0):
            m = n/10
            r = n%10
            if(r == 0) :
                amount = 0
            elif(r > 1):
                amount = factor
            else:
                amount = k%factor+1

            count += m*factor + amount
            factor *= 10
            n = n/10
        print count


if __name__ == '__main__':
    Test = Solution()
    print Test.countDigitOne(25)