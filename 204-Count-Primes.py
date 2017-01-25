def countPrimes(n):
    if n < 3:
        return 0
    res = [1] * n
    res[0] = 0
    res[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if res[i]:
            res[i+i::i] = [0] * len(res[i+i::i])
    return sum(res)


print(countPrimes(100))
