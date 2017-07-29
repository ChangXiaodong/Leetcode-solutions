def toHex(num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return '0'
    hex_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    to_hex_str = ''
    if num > 0:
        while num > 0:
            to_hex_str += str(hex_str[num % 16])
            num /= 16
        return to_hex_str[::-1]
    if num < 0:
        num = 4294967296 + num
        return toHex(num)


print(toHex())
