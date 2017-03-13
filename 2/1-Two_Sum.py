#coding=utf-8
'''
方法1.一个hash表
方法2：两个hash表
方法3：暴力搜索
'''
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if nums.__len__() == 2:
        return [0, 1]
    hash_map = {}
    hash_map2 = {}
    for i, v in enumerate(nums):
        if v in hash_map.keys():
            hash_map2[v] = i
        else:
            hash_map[v] = i
    for v in nums:
        num = target - v
        if num == v:
            if v in hash_map2:
                return [hash_map[v], hash_map2[v]]
        else:
            if num in hash_map.keys():
                return [hash_map[v], hash_map[num]]


def twoSum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if nums.__len__() == 2:
        return [0, 1]
    hash_map = {}
    for i, v in enumerate(nums):
        left = target - v
        if left in hash_map.keys():
            return [hash_map[left], i]
        else:
            hash_map[v] = i

print(twoSum1([4, 3, 2], 6))
