'''
夹逼法
三个数中第一个数固定，从1到n-1遍历。
后两个数用夹逼法，i in range(1,n-1),k in range(2,n)
若三个数和小于target， 提下界，若大于和，提上界

'''
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == target:
                return sum

            if abs(sum - target) < abs(result - target):
                result = sum

            if sum < target:
                j += 1
            elif sum > target:
                k -= 1
    return result


print(threeSumClosest([-1, 2, 1, -4], 1))
