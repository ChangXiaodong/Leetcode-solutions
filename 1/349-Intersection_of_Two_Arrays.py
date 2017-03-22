class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash_map = {}
        for v in nums1:
            hash_map[v] = hash_map.get(v, 0) + 1
        res = {}
        for v in nums2:
            if hash_map.get(v, "Null") != "Null" and res.get(v, "Null") == "Null":
                res[v] = 1
        return res.keys()