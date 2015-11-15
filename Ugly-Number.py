__author__ = 'Changxiaodong'
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        else:
            if num == 0:
                return True
            elif num%2 == 0:
                num /= 2
            elif num%3 == 0:
                num /= 3
            elif num%5 == 0:
                num /= 5
            else:
                return False
            return self.isUgly(num)