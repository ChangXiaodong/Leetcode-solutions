#coding=utf-8
'''
用哈希表
先遍历A、B 统计a+b的个数
再遍历C、D，看-(c+d)是否存在于哈希表中

ps：hash_map.get(key, "Nill") == "Nill" 效率优于 key in hash_map.keys()
'''
def fourSumCount(A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    if not A:
        return 0
    n = A.__len__()
    AB = {}
    for a in A:
        for b in B:
            AB[a + b] = AB.get(a + b, 0) + 1
    res = 0
    for c in C:
        for d in D:
            if AB.get(-c - d, "Nill") != "Nill":
                res += AB[-(c + d)]

    return res