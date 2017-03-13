#coding=utf-8
'''
使用一个栈，遍历s，
若该括号是左半部分，则将另一部分推入栈中。
若该括号是右半部分，若栈为空或栈顶元素跟他不一样(即上一个括号不是跟他配对的左半部分)，返回False
若遍历完后栈仍然不空，说明有括号没有配对，返回False
'''
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return False
    par_stack = []
    for p in s:
        if p == "(":
            par_stack.append(")")
        elif p == "[":
            par_stack.append("]")
        elif p == "{":
            par_stack.append("}")
        elif not par_stack or par_stack.pop() != p:
            return False
    return par_stack == []