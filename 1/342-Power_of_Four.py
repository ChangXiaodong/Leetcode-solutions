# coding=utf-8
'''
检查高4为是不是0001或0100，并且其余位都是0
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        length = (len(bin(num)) - 2) / 4
        one = 1 << length * 4
        four = 4 << length * 4
        return True if num == one or num == four else False
