# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node = root
        stack = []
        res = 0
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.left and node.left.left is None and node.left.right is None:
                res += node.left.val
            node = node.right
        return res