# coding=utf-8
'''
1.判断符号，如果有负号，把res添加负号，然后把两个数变成正数
2.求整数部分，如果没有小数部分就返回，如果有在res后面加“.”
3.构建一个哈希表，存余数和此时res的长度
4.用除法方法不断循环，直到余数重复出现在table中，说明找到了循环部分，取出余数的values，在res中插入括号。
'''
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return ""
        res = ""
        if numerator * denominator < 0:
            res = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator / denominator)
        num = numerator % denominator
        if num == 0:
            return res
        res += "."

        table = {num: len(res)}

        while num != 0:
            num *= 10
            res += str(num / denominator)
            num %= denominator
            if table.get(num, "Null") != "Null":
                index = table[num]
                res = res[:index] + "(" + res[index:] + ")"
                break
            else:
                table[num] = len(res)
        return res


solution = Solution()
print(solution.fractionToDecimal(-50, 8))
