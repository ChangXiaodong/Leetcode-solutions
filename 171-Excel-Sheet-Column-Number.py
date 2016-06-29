__author__ = 'Changxiaodong'
'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

'''
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