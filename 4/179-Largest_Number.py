# coding=utf-8
'''
s1 = "9",s2 = "30"
比较两个字符串时有两种可能，s1+s2大或者s2+s1大，将大的s1放到s2前面

cmp函数在python2中才有，cmp(y + x, x + y)，比较2个对象，前者小于后者返回-1，相等则返回0，大于后者返回1.
自己写一个help函数，实现cmp功能。当返回-1时，sort函数会把这两个元素点到位置
'''


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return ""
        res = [str(i) for i in nums]

        def help(x, y):
            if x + y < y + x:
                return 1
            else:
                return -1

        res.sort(cmp=lambda x, y: help(x, y))  # lambda 传入参数时，30为x，3为y
        if res[0] == "0":
            return "0"
        return "".join(res)


solution = Solution()
print(solution.largestNumber([3, 30, 34, 5, 9]))
