# coding=utf-8
'''
注意全为空格的情况和以空格结尾的情况，以及多个空格相连的情况
'''

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        cnt = 0
        flag = 1
        for i in range(len(s)):
            if s[i] == " ":
                if flag == 0:
                    cnt += 1
                    flag = 1
            else:
                flag = 0
        return cnt + 1 if flag == 0 else cnt