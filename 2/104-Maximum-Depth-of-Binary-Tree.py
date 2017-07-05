__author__ = 'Changxiaodong'
'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
import time


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nextlevel = [root]
        if (not root):
            return 0
        depth = 0
        while (nextlevel):
            bufnode = []
            for item in nextlevel:
                if item.left:
                    bufnode.append(item.left)
                if item.right:
                    bufnode.append(item.right)
            depth += 1
            nextlevel = bufnode
        return depth

    def nextRun(self, node):
        if node == None:
            return 0
        return max(1 + self.nextRun(node.left), 1 + self.nextRun(node.right))
