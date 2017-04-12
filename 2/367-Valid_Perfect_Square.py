# coding=utf-8
'''
方法1：二分查找，看mid的平方是不是num
方法2,：满足要求的数都是1+3+5+7+...的和
方法3：牛顿法  while(num(x*x-num)>1e-9)    
    { 
        x=(x+num/x)/2; 
    } 
'''
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0