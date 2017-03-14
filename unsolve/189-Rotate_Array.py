#coding=utf-8
'''
尤其注意
nums[:] = nums[-k:] + nums[:-k]
nums = nums[-k:] + nums[:-k]
两种写法区别。
第一种是将nums in place 改变
第二种没有改变旧的nums，创建了新的nums
'''
#89 ms
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if not nums or k == 0:
        return
    n = nums.__len__()
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]
    return nums

#222 ms
def rotate1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if not nums or k == 0:
        return
    n = nums.__len__()
    k = k % n
    for i in range(k):
        nums.insert(0, nums.pop())
#172
def rotate2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if not nums or k == 0:
        return
    n = nums.__len__()
    k = k % n
    for i in range(n - k):
        nums.append(nums.pop(0))

print(rotate([1, 2], 1))
