__author__ = 'chang'


def myAyoi(str):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    strLength = len(str)
    integer = 0
    symbal = ""
    in_flag = 0
    for i in range(strLength):
        if str[i] in num:
            integer = integer * 10 + num.index(str[i])
            in_flag = 1
        elif str[i] == "-" or str[i] == "+":
            if symbal == "" and i + 1 < strLength:
                if str[i + 1] in num:
                    symbal = str[i]
                else:
                    return 0
            else:
                return integer
        elif in_flag == 1:
            break
        elif str[i] != " ":
            return 0

    if symbal == "-":
        integer = -integer
    integer = min(integer, 2147483647)
    integer = max(integer, -2147483648)
    return integer


print myAyoi(" - 321")
