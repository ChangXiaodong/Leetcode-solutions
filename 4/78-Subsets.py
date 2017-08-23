# coding=utf-8
'''
方法1：遍历法。假设输入为[1, 2, 3].res初始化为[[]],遍历到1时，将1插入到res每个item中，结果为[[], [1]]
遍历到2时，将2插入到每个item中，结果为[[], [1], [1, 2], [2]]
遍历到3是，将3插入到每个item中，结果为[[], [1], [1, 2], [2], [3], [1, 3], [1, 2, 3], [2, 3]]

方法2：回溯法

方法3：位操作
 if we use the above example,
 1 appears once in every two consecutive subsets,
 2 appears twice in every four consecutive subsets,
 and 3 appears four times in every eight subsets,
 shown in the following (initially the 8 subsets are all empty):

[], [], [], [], [], [], [], []

[], [1], [], [1], [], [1], [], [1]

[], [1], [2], [1, 2], [], [1], [2], [1, 2]

[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]
'''


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []
    res = [[]]
    for v in nums:
        buf = res[:]
        for item in buf:
            res.append(item + [v])
    return res


def dfs(nums, index, path, res):
    res.append(path)
    for i in range(index, nums.__len__()):
        dfs(nums, i + 1, path + [nums[i]], res)


def subsets2(nums):
    if not nums:
        return []
    res = []
    dfs(nums, 0, [], res)
    return res

def subsets3(nums):
    if not nums:
        return []
    num_subset = 2 ** nums.__len__()
    res = [[] for _ in range(num_subset)]
    for i in range(nums.__len__()):
        for j in range(num_subset):
            if (j >> i) & 1:
                res[j].append(nums[i])
    return res


class Solution(object):
    def dfs(self, nums, k, buf, res, index):
        if buf.__len__() == k:
            res.append(buf[:])
            return
        for i in range(index, len(nums)):
            buf.append(nums[i])
            self.dfs(nums, k, buf, res, i + 1)
            buf.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums) + 1):
            buf = []
            self.dfs(nums, i, [], buf, 0)
            res.extend(buf)
        return res

print(subsets3([1, 2, 3]))
