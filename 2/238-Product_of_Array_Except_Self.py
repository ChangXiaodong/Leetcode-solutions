# coding=utf-8
'''
方法1：两个数组，一个存储从前向后遍历，不包括自身节点的积，一个从后向前不包括自身
方法2：不需要额外空间，先从前向后遍历，结果存储在res中，在从后向前遍历，累成在res中
O(n)
'''

def productExceptSelf1(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
        return []
    n = nums.__len__()
    if n == 1:
        return [0]
    front = [1 for _ in range(n)]
    back = [1 for _ in range(n)]
    for i in range(n - 2, -1, -1):
        front[i] = front[i + 1] * nums[i + 1]
    for i in range(1, n):
        back[i] = back[i - 1] * nums[i - 1]
    res = []
    for i in range(n):
        res.append(back[i] * front[i])
    return res

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
        return []
    n = nums.__len__()
    if n == 1:
        return [0]
    res = [0 for _ in range(n)]
    res[0] = 1
    for i in range(1, n):
        res[i] = res[i-1] * nums[i-1]
    right = 1
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res
