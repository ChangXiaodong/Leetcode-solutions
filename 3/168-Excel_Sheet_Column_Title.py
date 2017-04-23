# coding=utf-8
'''
Let's see the relationship between the Excel sheet column title and the number:

A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............   
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26
Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4

But how to get the column title from the number? We can't simply use the n%26 method because:

ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26

We can use (n-1)%26 instead, then we get a number range from 0 to 25.
'''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        res = self.convertToTitle((n - 1) / 26)
        res += chr((n - 1) % 26 + ord('A'))
        return res

    def convertToTitle1(self, n):
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        while n > 0:
            result.append(capitals[(n - 1) % 26])
            n = (n - 1) // 26
        result.reverse()
        return ''.join(result)



solution = Solution()
print(solution.convertToTitle1(27))
