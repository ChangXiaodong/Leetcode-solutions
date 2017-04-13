# coding=utf-8
'''
只需要检查根号num的数。每次加同时加i和num/i
'''
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        res = 0
        i = 2
        upper = num
        while i <= num ** 0.5:
            if num % i == 0:
                res += i + num / i
            i += 1
        res += 1
        return res == num