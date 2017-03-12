def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return -1
    c_dict = {}
    for c in s:
        c_dict[c] = c_dict.get(c, 0) + 1
    min_index = len(s) + 1
    for k, v in c_dict.items():
        if v == 1:
            min_index = min(s.index(k), min_index)
    return min_index if min_index <= len(s) else -1

def firstUniqChar1(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return -1
    n = len(s)
    char_list = [0 for _ in range(26)]
    start = ord("a")
    for v in s:
        char_list[ord(v) - start] += 1
    for i in range(n):
        if char_list[ord(s[i])-start] == 1:
            return i
    return -1



print(firstUniqChar1("leetcode"))

