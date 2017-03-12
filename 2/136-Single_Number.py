'''
^ => xor
14 ^ 14 ^16 = 16
'''


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return
    n = nums.__len__()
    for i in range(1, n):
        nums[i] = nums[i - 1] ^ nums[i]
    return nums[-1]
