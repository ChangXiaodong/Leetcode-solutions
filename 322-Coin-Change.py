def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    res = [amount + 1] * (amount + 1)
    res[0] = 0
    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if i >= coins[j]:
                res[i] = min(res[i], res[i - coins[j]] + 1)
    if res[amount] > amount:
        return -1
    else:
        return res[amount]



print(coinChange([186, 419, 83, 408], 6249))
