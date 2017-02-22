def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in xrange(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])  ###insert n
        perms = new_perms
    return perms


print permute([1,2,3])