__author__ = 'Changxiaodong'
import time
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        j = 0
        for i in range(len(s)-1,-1,-1):
            num+=pow(26,j)*(ord(s[i])-64)
            j+=1
        return num

if __name__ == "__main__":
    start = time.clock()
    test = Solution()
    print test.titleToNumber("")
    print time.clock() - start