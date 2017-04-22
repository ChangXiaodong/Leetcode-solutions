class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        min_radius = 0
        index = 0
        dis = 0
        if len(heaters) == 1:
            return max(houses[0]-heaters[0], houses[-1]-heaters[0])
        min_radius = abs(houses[0] - heaters[0])
        min_radius = max(abs(houses[-1] - heaters[-1]), min_radius)
        for i in range(1,len(heaters)):
            min_radius = max((heaters[i]-heaters[i-1])/2, min_radius)
        return min_radius



solution = Solution()
print(solution.findRadius([1,2,3,4], [1,10]))
