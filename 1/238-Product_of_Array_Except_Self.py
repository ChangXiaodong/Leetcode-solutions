#coding=utf-8
'''
要考虑数据内出现0的情况
将所有除0外的数相乘，并统计数组内0的个数
遍历数组，根据该数字是不是0以及0的个数判断最终结果

O(n)
'''

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    product = 1
    zeros = 0
    for v in nums:
        if v != 0:
            product *= v
        else:
            zeros += 1
    res = []
    for v in nums:
        if v == 0:
            if zeros == 1:
                res.append(product)
            elif zeros > 1:
                res.append(0)
        else:
            if zeros >= 1:
                res.append(0)
            else:
                res.append(product / v)
    return res