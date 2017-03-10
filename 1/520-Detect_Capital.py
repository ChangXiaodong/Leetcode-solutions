def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    if not word:
        return False
    if word.islower():
        return True
    if word.isupper():
        return True
    if word.istitle():
        return True
    return False


def detectCapitalUse1(word):
    """
    :type word: str
    :rtype: bool
    """
    if not word:
        return False
    all_capital = 0
    none_capital = 0
    upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    if word[0] not in upper:
        none_capital = 1
    for s in word[1:]:
        if s in upper:
            if none_capital == 1:
                return False
            all_capital = 1
        else:
            none_capital = 1
            if all_capital == 1:
                return False
    return True
