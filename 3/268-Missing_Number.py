#coding=utf-8
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

题目大意：给定一个数组，长度为n，数组内的数字从0-n，有一个缺失数字，找到这个缺失数字
'''
'''
异或 ^ 两个相同数字异或为0。如 [1,1,2] 则 1 ^ 1 ^ 2 = 2
计算方法：异或每个数字和index
index从0到n-1。
如果缺失的是n，数组内所有元素与index异或完结果为0，此时再异或n则为答案
如果缺失的不是n，数组内所有元素与index异或完结果为缺失数字x与n的异或，此时再异或n，剩下x为答案
'''
def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return
    res = nums[0] ^ 0
    for i in range(1, nums.__len__()):
        res = res ^ nums[i] ^ i
    return res ^ nums.__len__()

'''
哈希表
建立长度为n的哈希表
遍历nums，将其对应下标的数字置为1
搜索哈希表，若有数字为0，则对应的index为缺失数字
'''
def missingNumber1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return
    n = nums.__len__()
    num_list = [0 for _ in range(n + 1)]

    for v in nums:
        num_list[v] = 1
    for i, v in enumerate(num_list):
        if v == 0:
            return i
