'''
找到规律直接遍历
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        table = {"0": [], "1": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                 "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"],
                 "9": ["w", "x", "y", "z"]
                 }
        res = [""]
        for s in digits:
            ans = []
            for ch in table[s]:
                for item in res:
                    ans.append(item + ch)
            res = ans
        return res
