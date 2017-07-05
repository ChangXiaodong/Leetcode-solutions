'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex <= 0: return [1]
        if rowIndex == 1: return [1,1]
        triangle = [1,1]
        for j in range(2,rowIndex+1):
            res = [triangle[i]+triangle[i+1] for i in range(j-1)]
            triangle = [1]+res+[1]
        return triangle
if __name__ == "__main__":

    test = Solution()
    print  test.getRow(6)