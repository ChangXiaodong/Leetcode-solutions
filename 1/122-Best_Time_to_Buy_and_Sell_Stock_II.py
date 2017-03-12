#coding=utf-8
'''
如果当天的价格大于第二天的价格，并且已买入股票，在当天将股票卖出，如果没买就继续下一天
如果当天的价格小于等于第二天的价格，如果当前没买股票，就在今天买入，如果买了就继续下一天
最后检查股票是否卖出，如果没卖出就在最后一天卖了
'''
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    profit = 0
    buy = -1
    n = prices.__len__()
    for i in range(n - 1):
        if prices[i] > prices[i + 1]:
            if buy == -1:
                continue
            else:
                profit += prices[i] - buy
                buy = -1
        else:
            if buy == -1:
                buy = prices[i]
    if buy != -1:
        profit += prices[-1] - buy
    return profit