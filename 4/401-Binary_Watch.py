'''
方法1：遍历所有的时间数1的个数是不是和num相等
方法2：回溯
一共有10个可以放灯的位置，假设需要放3个
先把1放在第0位，然后让另2个在剩下的9个中combination
[1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
[1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
        .......
[1, 0, 1, 1, 0, 0, 0, 0, 0, 0]
[1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
        .......
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1]

combination基本做法  itertools.combinations(nums, 5) == dfs(nums, 0, res, [], 5)
def dfs(nums, index, res, buf, n):
    if buf.__len__() == n:
        res.append(buf[:])
        return
    else:
        for i in range(index, nums.__len__()):
            buf.append(nums[i])
            dfs(nums, i + 1, res, buf, n)
            buf.pop()
'''

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == num:
                    res.append(str(h) + ":" + str(m).zfill(2))
        return res

    def dfs(self, num, index, hr, mi, res):
        if num == 0:
            res.append(str(hr) + ":" + str(mi).zfill(2))
            return
        table = [1, 2, 4, 8, 16, 32, 1, 2, 4, 8]
        for i in range(index, 10):
            if i < 6:
                if mi + table[i] < 60:
                    self.dfs(num - 1, i + 1, hr, mi + table[i], res)
            else:
                if hr + table[i] < 12:
                    self.dfs(num - 1, i + 1, hr + table[i], mi, res)

    def readBinaryWatch1(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        self.dfs(num, 0, 0, 0, res)
        return res

def dfs(nums, index, res, buf, n):
    if buf.__len__() == n:
        res.append(buf[:])
        return
    else:
        for i in range(index, nums.__len__()):
            buf.append(nums[i])
            dfs(nums, i + 1, res, buf, n)
            buf.pop()

