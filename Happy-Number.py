__author__ = 'Changxiaodong'
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
