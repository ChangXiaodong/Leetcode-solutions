def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    if not nums:
        return False
    rot = 0
    for i in range(1, nums.__len__()):
        if nums[i] < nums[i - 1]:
            rot = i
            break
    if nums[0] < nums[-1]:
        rot = 0
    low = 0
    high = nums.__len__() - 1
    while low <= high:
        middle = (low + high) // 2
        realmid = (middle + rot) % nums.__len__()
        if target == nums[realmid]:
            return True
        if target < nums[realmid]:
            high = middle - 1
        else:
            low = middle + 1
    return False


def search1(nums, target):
    if not nums:
        return False
    lo = 0
    hi = nums.__len__() - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > nums[hi]:
            if nums[mid] > target and nums[lo] <= target:
                hi = mid
            else:
                lo = mid + 1
        elif nums[mid] < nums[hi]:
            if nums[mid] < target and nums[hi] >= target:
                lo = mid + 1
            else:
                hi = mid
        else:
            hi -= 1
    return nums[lo] == target


print(search([2, 2, 2, 2, 0, 2, 2, 2], 1))
print(search1([2, 2, 2, 2, 0, 2, 2, 2], 1))
