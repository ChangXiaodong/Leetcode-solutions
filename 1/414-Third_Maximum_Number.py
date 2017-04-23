class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)

        res = []
        for v in nums:
            if len(res) < 3:
                if v not in res:
                    res.append(v)
                    res.sort()
            else:
                if v > res[0] and v < res[1]:
                    res[0] = v
                elif v > res[1] and v < res[2]:
                    res[0] = res[1]
                    res[1] = v
                elif v > res[2]:
                    res[0] = res[1]
                    res[1] = res[2]
                    res[2] = v
        return res[0] if len(res) == 3 else max(res)