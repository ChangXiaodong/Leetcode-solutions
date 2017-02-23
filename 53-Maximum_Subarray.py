def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return
    max_sum = nums[0]
    result = max(nums)
    for i, v in enumerate(nums[1:]):
        max_sum = max([max_sum + v, v])
        result = max(result, max_sum)
    return result


print(maxSubArray([-1,-2,-3]))
