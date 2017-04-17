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
        res = str(numerator / denominator)
        if numerator * int(res) == denominator:
            return res
        res += "."
        recur = ""
        buf = ""
        cnt = 2
        while numerator % denominator != 0:
            residual = str(numerator % denominator)
            a = int(residual) * 10 / denominator
            if str(a) in recur and cnt > 0:
                buf += str(a)
                cnt -= 1
            else:
                if len(buf) > 0:
                    buf = set(buf)
                    recur.replace("", "")
                    res += recur + "({})".format(buf)
                    return res


            recur += str(a)
            numerator = int(residual) * 10 - a * denominator

        return res + recur



solution = Solution()
print(solution.fractionToDecimal(1,3))
