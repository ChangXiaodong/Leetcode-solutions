#coding=utf-8
'''
从个位开始计算，考虑进位
考虑几种特殊情况: "0" + "0", "1" + "1", "9" + "29", "9" + "99"
'''
def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    if not num1 and not num2:
        return ""
    if not num1:
        return num2
    if not num2:
        return num1
    s1_len = len(num1)
    s2_len = len(num2)
    num_map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    up = 0
    res = ""
    for i in range(max(s1_len, s2_len)):
        if i < s1_len:
            s1 = num1[s1_len - 1 - i]
        else:
            s1 = "0"
        if i < s2_len:
            s2 = num2[s2_len - 1 - i]
        else:
            s2 = "0"
        s1_int = num_map[s1]
        s2_int = num_map[s2]
        res_buf = s1_int + s2_int + up
        up = 0
        if res_buf >= 10:
            up = 1
            res_buf -= 10
        res += str(res_buf)
    if up == 1:
        res += "1"
    return res[::-1]