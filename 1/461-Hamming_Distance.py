class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:].zfill(32)
        y = bin(y)[2:].zfill(32)
        distance = 0
        for i in range(32):
            if x[i] != y[i]:
                distance += 1
        return distance