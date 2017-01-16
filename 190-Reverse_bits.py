def reverseBits(n):
    num = 0
    for i in range(32):
        if n & 1:
            num += 1
        n = n >> 1
        num = num << 1
    return num >> 1


def reverseBits1(n):
    return int(bin(n)[2:].zfill(32)[::-1], 2)


print(reverseBits(1))
print(reverseBits1(1))
