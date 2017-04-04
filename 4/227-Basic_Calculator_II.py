# coding=utf-8
'''
用一个栈，每次把数字存到栈里，如果数字前是减号，则存负数。
遇到乘法或除法时，从栈里弹出一个数字，然后向后找到一个数字完成运算。

ps：注意num1为负数时的计算，向上取整。 -3 // 2 = -1
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        stack = []
        i = 0
        num1 = ""
        num2 = ""
        sign = "+"
        while i < len(s):
            if s[i].isdigit():
                num1 += s[i]
            if not s[i].isdigit() or i == len(s) - 1:
                if num1:
                    if sign == "+":
                        stack.append(int(num1))
                    else:
                        stack.append(-int(num1))
                num1 = ""
                if s[i] == "-":
                    sign = "-"
                elif s[i] == "+":
                    sign = "+"
                elif s[i] == "*":
                    num1 = stack.pop()
                    i += 1
                    while i < len(s) and s[i].isdigit():
                        num2 += s[i]
                        i += 1
                    stack.append(int(num2) * num1)
                    i -= 1
                    num1 = ""
                    num2 = ""
                elif s[i] == "/":
                    num1 = stack.pop()
                    i += 1
                    while i < len(s) and s[i].isdigit():
                        num2 += s[i]
                        i += 1
                    if num1 < 0:
                        stack.append(-(abs(num1) / int(num2)))
                    else:
                        stack.append(num1 / int(num2))
                    i -= 1
                    num1 = ""
                    num2 = ""
            i += 1
        return sum(stack)

    def calculate1(self, s):
        if not s or len(s) == 0:
            return 0
        sign = "+"
        num = 0
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if not s[i].isdigit() and " " != s[i] or i == len(s) - 1:
                if sign == "-":
                    stack.append(-num)
                if sign == "+":
                    stack.append(num)
                if sign == "*":
                    stack.append(stack.pop() * num)
                if sign == "/":
                    if stack[-1] < 0:
                        stack.append(-(-stack.pop() / num))
                    else:
                        stack.append((stack.pop() / num))
                sign = s[i]
                num = 0
        return sum(stack)



solution = Solution()
print(solution.calculate1("14-3/2"))
