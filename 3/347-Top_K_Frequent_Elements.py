#coding=utf-8
'''
方法：哈希表+桶排序
遍历数组，统计每个数字出现的次数，存在哈希表中 value:frequent
将哈希表中的frequent进行桶排序，选出最大的k的
咋找哈希表，找到这k个frequent对应的value
'''
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hash_map = {}
    for v in nums:
        hash_map[v] = hash_map.get(v, 0) + 1
    res = []

    frequent = hash_map.values()
    for i in range(2):  #最大出现次数小于100次
        bucket = [[] for _ in range(10)]
        for v in frequent:
            bucket[v // 10 ** i % 10].append(v)
        frequent = [j for a in bucket for j in a]

    frequent[:] = frequent[-k:]
    for key, value in hash_map.items():
        if value in frequent:
            res.append(key)

    return res


print(topKFrequent([3, 0, 1, 0], 1))
