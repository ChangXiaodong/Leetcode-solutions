__author__ = 'Changxiaodong'
import time

class Solution(object):
    def RtoN(self, n):
        if n == "I":
            return 1
        elif n == "V":
            return 5
        elif n == "X":
            return 10
        elif n == "L":
            return 50
        elif n == "C":
            return 100
        elif n == "D":
            return 500
        elif n == "M":
            return 1000
        else:
            return 0

    def romaToInt(self, s):
        if len(s) == 1:
            return self.RtoN(s[0])
        a = self.RtoN(s[0])
        num = 0
        i = 1
        for i in range(1,len(s)):
            b = self.RtoN(s[i])
            if a < b:
                num -= a
            else:
                num += a
            a = b

        return num+self.RtoN(s[-1])

    def romaToInt1(self,s):
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, '0': 0}
        return sum([romanDict[c] if romanDict[c] >= romanDict[d] else romanDict[c]*-1 for c,d in zip(s, (s + '0')[1:])])
        #上面这句话写成正常形式
        # num = 0
        # for c,d in zip(s, (s + '0')[1:]):
        #     if romanDict[c] >= romanDict[d]:
        #         num += sum([romanDict[c]])
        #     else:
        #         num += sum([romanDict[c]*-1])
        # print num

if __name__ == "__main__":
    start = time.clock()
    test = Solution()
    print test.romaToInt("CCVII")
    print test.romaToInt1("CCVII")
    print time.clock() - start
