# coding=utf-8
'''
题目：在nums中找到两个相等的数，看对应的index差值的绝对值是否不大于k

1：排序，然后从1，n，在1：1+k， 2：2+k， 内二分查找是否满足条件

2：哈希表：特殊情况。【1，2，3，4，1，2，1】，k=2，相等的1的index有0，4，6。在遍历到0和4时不满足条件，此时把table中1对应的index
更新为4
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        table = {}
        for i, v in enumerate(nums):
            if table.get(v, "Null") != "Null":
                if abs(i - table[v]) <= k:
                    return True
            table[v] = i
        return False
