__author__ = 'Changxiaodong'
class Solution(object):
    def countDigitOne(self,k):
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



if __name__ == "__main__":
    test = Solution()
    test.countDigitOne(1)