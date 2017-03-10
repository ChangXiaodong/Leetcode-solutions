def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    if not findNums:
        return []
    if not nums:
        return []
    res = [-1 for _ in range(findNums.__len__())]
    for j, v in enumerate(findNums):
        for i in range(nums.index(v) + 1, nums.__len__()):
            if nums[i] > v:
                res[j] = nums[i]
                break
    return res