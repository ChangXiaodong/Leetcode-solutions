'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''
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


