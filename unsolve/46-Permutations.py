# coding=utf-8
'''
方法1：从nums内第三个数开始，插入到之前结果的缝隙中，组成新的排列，知道numds内数字全部插完为止
eg:前两个数全排列为[[|0|1|], [|1|0|]]，第三个数可以在|位置插入，一共用六种组合】

方法2：定义一个used数组，记录当前数字是否在item中，如果不在，插入到item中，若item长度等于nums，说明所有数字插入完毕，将
item加到结果res中，item弹出最后一个数字，继续遍历。这种方法会首先固定第一个数字，将后面的数字全排列，
'''


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []
    n = nums.__len__()
    if n == 1:
        return nums
    buf_ans = [[nums[0], nums[1]], [nums[1], nums[0]]]
    res = buf_ans
    index = 2
    for v in nums[2:]:
        res = []
        for buf in buf_ans:
            for i in range(index + 1):
                res.append(buf[:i] + [v] + buf[i:])
        index += 1
        buf_ans = res
    return res


def permute1(nums):
    def helper(num, used, item, res):
        if item.__len__() == num.__len__():
            res.append(item[:])
            return
        for i in range(num.__len__()):
            if not used[i]:
                used[i] = True
                item.append(num[i])
                helper(num, used, item, res)
                item.pop()
                used[i] = False

    if not nums:
        return nums
    res = []
    used = [False for _ in range(nums.__len__())]
    item = []
    helper(nums, used, item, res)
    return res


print(permute1([0, 1, 2]))
