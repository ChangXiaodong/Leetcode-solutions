def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return
    max_sum = nums[0]
    result = max(nums)
    for v in nums[1:]:
        max_sum = max(max_sum + v, v)
        result = max(result, max_sum)
    return result


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
