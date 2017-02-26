def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if prices.__len__() < 2:
        return 0
    max_profit = 0
    min_buy = prices[0]
    for i, v in enumerate(prices[1:]):
        max_profit = max(v - min_buy, max_profit)
        min_buy = min(min_buy, v)
    return max_profit


print(maxProfit([7,1,5,3,6,4]))
