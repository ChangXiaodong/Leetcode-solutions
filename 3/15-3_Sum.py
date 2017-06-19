# coding=utf-8
'''
先把数组排序，然后从第一个开始遍历，设置三个指针，第一个指针是当前遍历的数，第二个是当前遍历的数+1，第三个是最后一个数。
计算这三个数的和，如果等于0就加到结果中，然后去重。如果小于0，第二个指针后移，如果大于零，第三个指针前移。
注意去掉重复的数
'''
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

print(threeSum([-1, 0, 1, 2, -1, -4]))
