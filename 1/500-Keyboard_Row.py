def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    res = []
    for word in words:
        row = 0
        for ch in word:
            if ch in row1:
                if row == 0:
                    row = 1
                elif row != 1:
                    row = 4
            if ch in row2:
                if row == 0:
                    row = 2
                elif row != 2:
                    row = 4
            if ch in row3:
                if row == 0:
                    row = 3
                elif row != 3:
                    row = 4
        if row != 4:
            res.append(word)
    return res
