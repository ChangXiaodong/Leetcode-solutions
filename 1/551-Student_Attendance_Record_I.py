class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        a_cnt = 0
        l_cnt = 0
        for v in s:
            if v == "A":
                a_cnt += 1
                if a_cnt > 1:
                    return False
            if v == "L":
                l_cnt += 1
                if l_cnt > 2:
                    return False
            else:
                l_cnt = 0
        return True