from collections import deque


def first_character(string):
    new_string = ""
    stack = deque()
    for s in string:
        if s not in new_string:
            new_string += s
            stack.append(s)
        else:
            if s in stack:
                stack.remove(s)
    if stack:
        return stack.popleft()
    else:
        return ""


print(first_character("google"))
