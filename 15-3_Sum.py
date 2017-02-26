def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    result = []
    n = nums.__len__()
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        k = i + 1
        j = n - 1
        while k < j:
            sum_3 = nums[i] + nums[k] + nums[j]
            if sum_3 == 0:
                result.append([nums[i], nums[k], nums[j]])
                while k < j and nums[k] == nums[k + 1]:
                    k += 1
                while k < j and nums[j] == nums[j - 1]:
                    j -= 1
            if sum_3 < 0:
                k += 1
            else:
                j -= 1

    return result




print(threeSum([0, 0, 0, 0]))
