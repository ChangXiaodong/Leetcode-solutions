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


def strStr1(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

#kmp
def strStr2(haystack, needle):
    if not haystack and not needle:
        return 0
    if not needle:
        return 0
    n1 = len(haystack)
    n2 = len(needle)
    table = [0 for _ in range(n2)]

    i = 1
    j = 0
    # build table
    while i < n2:
        if needle[i] != needle[j]:
            if j > 0:
                j = table[j - 1]
            else:
                i += 1
        else:
            table[i] = j + 1
            j += 1
            i += 1
    index1 = 0
    index2 = 0
    # search
    while index1 < n1:
        if haystack[index1] == needle[index2]:
            if index2 == n2 - 1:
                return index1 + 1 - n2
            else:
                index1 += 1
                index2 += 1
        else:
            if index2 == 0:
                index1 += 1
            else:
                index2 = table[index2 - 1] #index2 = index2 - (index2 - table[index2 - 1])
    return -1

#bm
def strStr3(haystack, needle):
    if not haystack and not needle:
        return 0
    if not needle:
        return 0
    n = len(haystack)
    m = len(needle)
    right = {}
    for i in range(len(needle)):
        right[needle[i]] = i
    i = 0
    while i <= n - m:
        skip = 0
        j = m - 1
        while j >= 0:
            if haystack[i+j] != needle[j]:
                skip_buf = right.get(haystack[i+j], -1)
                skip = j - skip_buf
                if skip < 1:
                    skip = 1
                break
            j -= 1
        if skip == 0:
            return i
        i += skip
    return -1





print(strStr3("here is a simple example","example"))
