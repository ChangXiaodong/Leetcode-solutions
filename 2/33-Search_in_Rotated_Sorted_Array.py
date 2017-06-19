def search(nums, target):
    if target not in nums:
        return -1
    else:
        return nums.index(target)


def binarySearch(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[hi] < nums[mid]:
            lo = mid + 1
        else:
            hi = mid
    rot = lo
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        realmid = (mid + rot) % len(nums)
        if target == nums[realmid]:
            return realmid
        elif target > nums[realmid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


print(binarySearch([4, 5, 6, 7, 0, 1, 2, 3], 5))
