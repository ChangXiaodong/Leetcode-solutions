def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    from collections import deque
    if not s:
        return True
    buf = []
    rev = deque()
    for c in s:
        if c.isalpha() or c.isdigit():
            buf.append(c.lower())
            rev.appendleft(c.lower())
    return "".join(buf) == "".join(rev)

def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleanlist = [c for c in s.lower() if c.isalnum()]
        return cleanlist == cleanlist[::-1]


