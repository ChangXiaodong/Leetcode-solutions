def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []
    n = nums.__len__()
    if n == 1:
        return nums
    buf_ans = [[nums[0], nums[1]], [nums[1], nums[0]]]
    res = buf_ans
    index = 2
    for v in nums[2:]:
        res = []
        for buf in buf_ans:
            for i in range(index + 1):
                res.append(buf[:i] + [v] + buf[i:])
        index += 1
        buf_ans = res
    return res


print(permute([0,1]))
