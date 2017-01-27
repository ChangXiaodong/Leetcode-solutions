def lexicalOrder(n):
    """
    :type n: int
    :rtype: List[int]
    """
    result = []

    def solve(m):
        result.append(m)
        if m * 10 <= n:
            solve(m * 10)
        if m < n and m % 10 < 9:
            solve(m + 1)

    solve(1)
    return result


def lexicalOrder1(n):
    result = []
    stack = [1]
    while stack:
        num = stack.pop()
        result.append(num)
        if num < n and num % 10 < 9:
            stack.append(num + 1)
        if num * 10 <= n:
            stack.append(num * 10)
    return result


print(lexicalOrder1(49999))
