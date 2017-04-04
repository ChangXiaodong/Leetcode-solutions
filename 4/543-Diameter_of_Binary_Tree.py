# coding=utf-8
'''
遍历每个节点，找到左子树的最大深度，又子树的最大深度。则以该节点为跟节点的子树diameter为left_depth + right_depth + 1
难点在要从叶子节点开始计算深度，不是从root开始计算深度。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def depth(self, node):
        if not node:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        self.res = max(self.res, left + right + 1)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.depth(root)
        return self.res - 1

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node6
node6.left = node8
node5.right = node7
node7.right = node9

solution = Solution()
print(solution.diameterOfBinaryTree(node1))
