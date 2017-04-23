class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ch = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "k", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z"]
        res = ""

        if n <= 26:
            return ch[(n-1) % 26]
        first = ch[(n-1) / 26 - 1]
        n = (n-1) % 26
        second = ch[n]
        return first + second


solution = Solution()
print(solution.convertToTitle(26))
