'''
中序遍历，获得排序的数组后查找相邻两个差值
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        stack = []
        node = root
        res = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right

        ans = float("inf")
        for i in range(1, res.__len__()):
            ans = min(ans, abs(res[i] - res[i - 1]))
        return ans




