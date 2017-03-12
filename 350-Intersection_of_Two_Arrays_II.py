# coding=utf-8
'''
遍历较小的数组，逐个检查该元素是否存在于另一个数组中
'''


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    if not nums1:
        return []
    if not nums2:
        return []
    if nums1.__len__() > nums2.__len__():
        n = nums2.__len__()
        bigger = 1
    else:
        n = nums1.__len__()
        bigger = 2
    res = []
    if bigger == 1:
        for i in range(n):
            if nums2[i] in nums1:
                res.append(nums2[i])
                nums1.remove(nums2[i])
    else:
        for i in range(n):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.remove(nums1[i])
    return res


# hash map

def intersect1(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    if not nums1 or not nums2:
        return []
    char_dict = {}
    for v in nums1:
        char_dict[v] = char_dict.get(v, 0) + 1
    res = []
    for v in nums2:
        if v in char_dict.keys() and char_dict[v] > 0:
            res.append(v)
            char_dict[v] -= 1
    return res




'''
Counter统计出列表中每个元素的个数，以hashmap形式存储
c1 & c2求出两个列表中交集的元素及其个数，以hashmap形式存储
将c1 & c2展开成list
'''
from collections import Counter
def intersect2(nums1, nums2):
    c1, c2 = Counter(nums1), Counter(nums2)
    res = []
    for key, value in (c1 & c2).items():
        res.extend([key] * value)
    return res

print(intersect2([1, 2, 2, 4, 5, 6, 3], [2, 2, 5, 4]))
