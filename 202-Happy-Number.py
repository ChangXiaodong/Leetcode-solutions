__author__ = 'Changxiaodong'
'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
import time
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.resultbuf = []
        return self.happyNumber(n)

    def happyNumber(self,n):
        result = 0
        num = n
        while num:
            result += pow(num%10,2)
            num /= 10
        #Solution1
        a = result
        if(a==1):
            return True
        elif(a<10 and a != 1):
            return False
        else:
            return self.isHappy(a)
        #Solution2
        # if result in self.resultbuf:
        #     print "not"
        #     return False
        # else:
        #     if result == 1:
        #         print "happy"
        #         return True
        #     else:
        #         self.resultbuf.append(result)
        #         return self.happyNumber(result)


if __name__ == "__main__":
    start = time.clock()
    test = Solution()
    print test.isHappy(19)
    print time.clock() - start
