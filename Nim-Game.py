__author__ = 'Changxiaodong'
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<1):
            return False
        elif(n<4):
            return True
        elif(n%4==0):
            return False
        else:
            return True
if __name__ == "__main__":
    test = Solution()
    print test.canWinNim(4)