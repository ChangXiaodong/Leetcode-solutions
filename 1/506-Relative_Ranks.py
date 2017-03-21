class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        rank = sorted(nums)[::-1]
        res = [0 for _ in range(nums.__len__())]
        for i in range(rank.__len__()):
            if i == 0:
                res[nums.index(rank[i])] = "Gold Medal"
            elif i == 1:
                res[nums.index(rank[i])] = "Silver Medal"
            elif i == 2:
                res[nums.index(rank[i])] = "Bronze Medal"
            else:
                res[nums.index(rank[i])] = str(i + 1)
        return res

