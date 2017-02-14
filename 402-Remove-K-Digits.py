def removeKdigits(num, k):
    out = []
    for d in num:
        while k and out and out[-1] > d:
            out.pop()
            k -= 1
        out.append(d)
    return ''.join(out[:-k or None]).lstrip('0') or '0'

print(removeKdigits('1432219', 3))
