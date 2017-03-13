def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not haystack and not needle:
        return 0
    if not needle:
        return 0
    n = len(haystack)
    n2 = len(needle)
    for i in range(n):
        index = i
        for j in range(n2):
            if haystack[index] == needle[j]:
                if j == (n2 - 1):
                    return i
                if index < n - 1:
                    index += 1
                else:
                    return -1
            else:
                break
    return -1