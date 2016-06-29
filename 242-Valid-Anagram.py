__author__ = 'Changxiaodong'
'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
'''
import time
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        x=sorted(s)
        y=sorted(t)

        print x==y

        for i in range(len(x)):
            if x[i] != y[i]:
                return False
        return True

if __name__ == "__main__":
    start = time.clock()
    test = Solution()
    print test.isAnagram('abda','dbac')
    print time.clock() - start