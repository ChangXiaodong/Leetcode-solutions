# coding=utf-8
'''
注意负数除法！！！
用int(math.modf(x)[1])
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return
        i = 0
        ops = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}
        while i < len(tokens):
            try:
                tokens[i] = int(tokens[i])
            except:
                op = tokens.pop(i)
                i -= 2
                num1 = int(tokens.pop(i))
                num2 = int(tokens.pop(i))
                if op == "/" and num1 * num2 < 0:
                    tokens.insert(i, -ops[op](abs(num1), abs(num2)))
                else:
                    tokens.insert(i, ops[op](num1, num2))
            i += 1
        return tokens[0]
