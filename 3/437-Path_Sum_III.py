# coding=utf-8
'''
后序遍历，求出左子节点可能出现的和，右子节点可能出现的和，本节点的和分别和左右子节点可能出现的和相加，如果等于sum，则计数+1
如果本节点的和自身等于sum，计数+1
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def post_order(self, node, sum):
        if not node:
            return []
        left = self.post_order(node.left, sum)
        right = self.post_order(node.right, sum)
        res = []
        for v in left:
            res.append(v + node.val)
            if node.val + v == sum:
                self.cnt += 1
        for v in right:
            res.append(v + node.val)
            if node.val + v == sum:
                self.cnt += 1
        if node.val == sum:
            self.cnt += 1
        res.append(node.val)
        return res

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.cnt = 0
        self.post_order(root, sum)
        return self.cnt


