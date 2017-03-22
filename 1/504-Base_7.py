class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            res = "-"
            num = -num
        else:
            res = ""
        ans = ""
        buf = num
        while buf >= 7:
            ans += str(buf % 7)
            buf = buf // 7
        ans += str(buf)
        res += ans[::-1]
        return res