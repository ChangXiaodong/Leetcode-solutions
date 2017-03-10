def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
        return []
    nums.sort()
    res = []
    for i in range(1, nums.__len__()):
        if nums[i - 1] == nums[i]:
            res.append(nums[i])
    return res

'''
// when find a number i, flip the number at position i-1 to negative.
// if the number at position i-1 is already negative, i is the number that occurs twice.
without extra space and in O(n) runtime
'''
def findDuplicates1(nums):
    if not nums:
        return []
    res = []
    for v in nums:
        v = abs(v)
        if nums[v - 1] < 0:
            res.append(v)
        else:
            nums[v - 1] = -nums[v - 1]
    return res


print(findDuplicates1([4, 3, 2, 7, 8, 2, 3, 1]))
