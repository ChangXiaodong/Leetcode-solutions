def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 0
    b = 0
    for i, v in enumerate(nums):
        if i % 2 == 0:
            a = max(a + nums[i], b)
        else:
            b = max(b + nums[i], a)
    return max(a, b)


def rob1(nums):
    if not nums:
        return 0
    n = len(nums)
    if n <= 2:
        return max(nums)

    last = nums[0]
    now = max(nums[0], nums[1])
    for i in range(2, n):
        last, now = now, max(nums[i] + last, now)
    return now


def equal_rob1(nums):
    if not nums:
        return 0
    n = len(nums)
    if n <= 2:
        return max(nums)
    res = [0 for _ in range(n)]

    res[0] = nums[0]
    res[1] = max(nums[0], nums[1])
    for i in range(2, n):
        res[i] = max(nums[i] + res[i - 2], res[i - 1])
    return max(res)


def rob2(nums):
    if not nums:
        return 0
    n = len(nums)
    if n <= 2:
        return max(nums)
    include = 0
    exclude = 0
    for v in nums:
        temp = include
        include = exclude + v
        exclude = max(temp, exclude)
    return max(include, exclude)


print(rob([30, 2, 3, 20, 5]))
print(rob1([30, 2, 3, 20, 5]))
print(equal_rob1([30, 2, 3, 20, 5]))
print(rob2([30, 2, 3, 20, 5]))
