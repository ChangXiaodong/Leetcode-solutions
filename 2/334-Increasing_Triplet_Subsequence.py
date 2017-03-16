#coding=utf-8
'''
按顺序遍历nums，不断更新最小的数
如果这个数比最大的数小，说明这个数是目前倒数第二大的数， 也就是三个数里面中间那个
如果后面的数比high大，就是三个数里面最大的数
'''
def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    low = float("inf")
    high = low
    for v in nums:
        if v <= low:
            low = v
        elif v <= high:
            high = v
        else:
            return True
    return False


print(increasingTriplet([1,0,0,10,0,100000000]))
