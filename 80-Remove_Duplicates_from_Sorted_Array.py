def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    i = j = 0
    n = nums.__len__()
    while j < n:
        j = i
        while j < n and nums[i] == nums[j]:
            j += 1
        if j - i > 2:
            n -= j - i - 2
            for m in range(j - i - 2):
                nums.pop(i)
                j -= 1
        i = j
    return nums.__len__(), nums

def removeDuplicates1(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i


print(removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3]))
print(removeDuplicates1([1, 1, 1, 2, 2, 2, 3, 3]))
