class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        min_price = float("inf")
        max_price = 0
        for v in prices:
            min_price = min(min_price, v)
            max_price = max(max_price, v - min_price)
        return max_price

    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = [0]
        if len(prices) < 2:
            return 0
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i - 1])
        res = 0
        buf = 0
        for i in range(len(diff)):
            buf = buf + diff[i]
            if buf <= 0:
                buf = 0
            res = max(res, buf)
        return res