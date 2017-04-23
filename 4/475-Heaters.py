# coding=utf-8
'''
二分查找：遍历每一个房子，用二分查找找到距离这个房子最近的两个heater，计算这个房子到这两个最近
heater的距离，取最小距离。最后结果为这些最小距离里面的最大值。注意左边或右边没有
heater的情况
'''
class Solution(object):
    def find(self, heaters, house):
        low = 0
        high = len(heaters) - 1
        if heaters[-1] < house:
            return high, high
        if heaters[0] > house:
            return low, low
        while low < high:
            middle = (low + high) / 2
            if heaters[middle] == house:
                return middle, middle
            if heaters[middle] > house:
                high = middle - 1
            else:
                low = middle + 1
        if heaters[low] < house:
            return low, low + 1
        else:
            return low, low - 1

    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        min_radius = 0
        heaters.sort()
        for h in houses:
            h1, h2 = self.find(heaters, h)
            min_radius = max(min_radius, min(abs(heaters[h1] - h), abs(heaters[h2] - h)))
        return min_radius


solution = Solution()
print(solution.findRadius([1], [1, 2, 3, 4]))
