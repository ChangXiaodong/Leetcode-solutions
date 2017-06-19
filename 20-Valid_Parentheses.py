def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return True
    par_dict = {"(": ")", "[": "]", "{": "}"}
    next_par = par_dict.get(s[0], "")
    if not next_par:
        return False
    n = len(s)
    count = 0
    for j in range(1, n):
        if s[j] == s[0]:
            count += 1
        elif s[j] == next_par and count > 0:
            count -= 1
        elif s[j] == next_par and count == 0:
            if j - 1 < 1:
                return True and isValid(s[j + 1:])
            else:
                return isValid(s[1:j]) and isValid(s[j + 1:])
    return False


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        parent = {
            "(": ")", "[": "]", "{": "}"
        }
        for i in range(len(s)):
            cur = parent.get(s[i], '')
            if cur:
                stack.append(cur)
            elif not stack or s[i] != stack.pop():
                return False
        if stack:
            return False
        return True


print(isValid("[{[]{}}[})}]{[]}[)(()]{}{{]()}}](}[("))
