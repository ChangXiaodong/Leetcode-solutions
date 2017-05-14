# coding=utf8
'''
题意是n=1时输出字符串1；n=2时，数上次字符串中的数值个数，
因为上次字符串有1个1，所以输出11；n=3时，由于上次字符是11，
有2个1，所以输出21；n=4时，由于上次字符串是21，有1个2和1个1，
所以输出1211。
'''


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    if n <= 0:
        return ""
    if n == 1:
        return "1"
    last_str = "11"
    for i in range(n - 2):
        count = 1
        str_buf = ""
        # 遍历上一个字符串内每个字符，并计数
        for j in range(len(last_str) - 1):
            if last_str[j] == last_str[j + 1]:
                count += 1
            else:
                str_buf += str(count) + last_str[j]
                count = 1
        # 处理最末尾字符串
        str_buf += str(count) + last_str[-1]
        last_str = str_buf
    return last_str


print(countAndSay(5))
