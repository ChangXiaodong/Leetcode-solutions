# coding=utf-8
'''
二分查找，注意移出，除0，和负数
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2147483647
        if dividend ^ divisor < 0:
            negative = 1
        else:
            negative = 0

        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor:
            return 0
        low = 0
        high = dividend

        while low <= high:
            middle = (low + high) >> 1
            if middle * divisor == dividend:
                if negative == 1:
                    middle = -middle
                if middle > 2147483647:
                    middle = 2147483647
                return middle
            if middle * divisor < dividend:
                low = middle + 1
            else:
                high = middle - 1
        if negative == 1:
            high = -high
        if high > 2147483647:
            high = 2147483647
        return high

