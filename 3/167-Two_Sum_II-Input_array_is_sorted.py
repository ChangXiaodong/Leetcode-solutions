'''
方法1：双指针，小于target，左指针加1，大于target又指针加1
方法2：哈希表，跟排不排序没关系
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = numbers.__len__() - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            if total < target:
                low += 1
            else:
                high -= 1

    def twoSum1(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(numbers.__len__()):
            buf = target - numbers[i]
            if hash_map.get(buf, "Null") != "Null":
                return [hash_map[buf] + 1, i + 1]
            hash_map[numbers[i]] = i




solution = Solution()
print(solution.twoSum([3,24,50,79,88,150,345], 200))
