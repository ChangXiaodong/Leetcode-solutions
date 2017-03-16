def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
        return 0
    for i, v in enumerate(nums):
        if target <= v:
            return i
    return nums.__len__()