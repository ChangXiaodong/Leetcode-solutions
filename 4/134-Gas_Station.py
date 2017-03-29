# coding=utf-8
'''
方法1：计算gas[i]-cost[i] 如果小于0，start = i+1。然后从start搜索一圈，看是否能够完成
方法2：计算gas[i]-cost[i] 如果小于0，start = i+1。同时将之前的和保存为total。如果最后total大于等于0，说明能完成，返回start，否则-1
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas:
            return False
        if not cost:
            return True
        n = gas.__len__()
        start = 0
        cur = 0
        iter = 0
        while True:
            cur += gas[iter] - cost[iter]
            iter += 1

            if cur < 0:
                if iter <= start:
                    start += 1
                else:
                    start = iter
                cur = 0
            else:
                iter = iter % n
                if iter == start:
                    return start
            iter = iter % n
            if start == n:
                return -1

    def canCompleteCircuit1(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas:
            return False
        if not cost:
            return True
        minus = 0
        start = 0
        total = 0
        for i in range(gas.__len__()):
            minus += gas[i] - cost[i]
            if minus < 0:
                total += minus
                minus = 0
                start = i+1
        total += minus
        return start if total >= 0 else -1


solution = Solution()
print(solution.canCompleteCircuit([3, 4], [3, 4]))
