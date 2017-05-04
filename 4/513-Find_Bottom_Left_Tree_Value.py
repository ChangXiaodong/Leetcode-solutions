# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, node, l):
        if not node:
            return
        self.dfs(node.left, l + 1)
        if l > self.level:
            self.res = node.val
            self.level = l
        self.dfs(node.right, l + 1)

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.level = -1
        self.res = 0
        self.dfs(root, 0)
        return self.res

node1 = TreeNode(2)
# node2 = TreeNode(1)
# node3 = TreeNode(3)
# node1.left = node2
# node1.right = node3
solution = Solution()
print(solution.findBottomLeftValue(node1))

