#codinf=utf-8
'''
从第一个点开始遍历，计算之后每一个点与这个点的距离，存储在哈希表中。
第一个点遍历完后，根据距离相等的点的个数计算可以组合的结果，res = 相等的个数*(相等的个数-1)。
'''
def distance(i, j):
    return ((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2)

def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    if not points:
        return 0
    hash_map = {}
    res = 0
    for i in points:
        for j in points:
            if i != j:
                dis = distance(i, j)
                hash_map[dis] = hash_map.get(dis, 0) + 1
        for d in hash_map.keys():
            res += hash_map[d] * (hash_map[d] - 1)
        hash_map.clear()
    return res