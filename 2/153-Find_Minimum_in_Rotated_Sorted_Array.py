# coding=utf-8
'''
二分查找，注意更新low和high的条件
'''


def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return
    low = 0
    high = nums.__len__() - 1
    while low < high:
        middle = (low + high) // 2
        if nums[middle] > nums[high]:
            low = middle + 1
        else:
            high = middle
    return nums[low]


def findMin1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return
    low = 0
    high = nums.__len__() - 1
    while low < high:
        middle = (low + high) / 2
        if nums[middle] > nums[high]:
            low = middle + 1
        else:
            high = middle - 1
    return nums[low]


print(findMin1([2, 1]))
