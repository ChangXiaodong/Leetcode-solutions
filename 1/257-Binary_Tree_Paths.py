# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, path):
        if not node:
            return
        path += str(node.val)
        if not node.left and not node.right:
            self.res.append(path)
            return
        self.dfs(node.left, path + "->")
        self.dfs(node.right, path + "->")

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        self.dfs(root, "")
        return self.res
