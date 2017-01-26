def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for curr_num in nums:
        count = 0
        for find_num in nums:
            if curr_num == find_num:
                count += 1
                if count > 1:
                    return curr_num


def findDuplicate1(nums):
    slow, fast, finder = nums[0], nums[nums[0]], 0

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    while slow != finder:
        slow = nums[slow]
        finder = nums[finder]

    return finder


print(findDuplicate1([1, 3, 4, 2, 5, 6, 7, 2]))
