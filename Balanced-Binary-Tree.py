__author__ = 'Changxiaodong'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        leftdepth = 0
        rightdepth = 0
        if not root:
            return True
        if root.left:
            leftdepth = self.getHeight(root.left)
        if root.right:
            rightdepth = self.getHeight(root.right)
        if abs(leftdepth - rightdepth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False

    def getHeight(self, node):
        if not node:
            return 0
        return max(1+self.getHeight(node.left),1+self.getHeight(node.right))

