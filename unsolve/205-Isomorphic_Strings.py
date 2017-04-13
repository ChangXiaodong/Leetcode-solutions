class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(len(t)):
            s = s.replace(s[i], str(i))
            t = t.replace(t[i], str(i))
        return t == s

solution = Solution()
print(solution.isIsomorphic("aaaaabbbbbcccccdddddeeeee", "pppppqqqqqrrrrrsssssttttt"))