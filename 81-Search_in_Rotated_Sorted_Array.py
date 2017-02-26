'''
与没有重复的情况不同的地方在于不确定什么时候更新low和high，没有办法准确找出rotate点。
有两种办法：
1> 用O(n)时间遍历数组，找到rotate点，再用二分查找
2> 平均复杂度O(log(n))，最坏复杂度O(n),在查找过程中选择更新low和high的方法。
把一个rotated数组看成两部分，大端和小端。如[4 5 6 7 0 1 2]， 大端为[4 5 6 7]，小端为[0 1 2]
首先判断middle实在大端部分还是小端部分，如果在大端部分，在判断target是不是落在大端，根据结果更新low和high，若middle在
小端，判断target是否落在小端，并更新low和high。
如果直到lo==high都没有找到target，则target不存在。

'''
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
