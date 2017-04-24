class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, a2 = a.split("+")
        b1, b2 = b.split("+")
        res1 = int(a1) * int(b1) + int(a2[:-1]) * int(b2[:-1]) * -1
        res2 = int(a1) * int(b2[:-1]) + int(a2[:-1]) * int(b1)
        return str(res1) + "+" + str(res2) + "i"