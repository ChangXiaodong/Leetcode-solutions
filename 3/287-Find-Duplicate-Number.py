#coding=utf-8
'''
方法一：双指针
方法二：二分搜索，无排序数组，数组值不用index进行搜索
'''
def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for curr_num in nums:
        count = 0
        for find_num in nums:
            if curr_num == find_num:
                count += 1
                if count > 1:
                    return curr_num


def findDuplicate1(nums):
    slow, fast, finder = nums[0], nums[nums[0]], 0

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    while slow != finder:
        slow = nums[slow]
        finder = nums[finder]

    return finder

def findDuplicate2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    low = 1
    high = nums.__len__() - 1
    while low <= high:
        mid = (low + high) // 2
        cnt = 0
        for v in nums:
            if v <= mid:
                cnt += 1
        if cnt <= mid:
            low = mid + 1
        else:
            high = mid - 1
    return low


print(findDuplicate2([2,2,3,4,5,6,7,1]))
