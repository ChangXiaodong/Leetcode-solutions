# coding=utf-8
'''
方法1：如果是查找树，中序遍历的顺序应该是升树，并且不包含重复数字。（不重复是这个题目的特殊要求）。将中序遍历的结果和sort后的结果对比，
并且查找是否有重复的元素

方法2：前序遍历，验证以该节点为跟节点的子树是否为有效查找树。每次递归时传入有效的范围，如果node的值超过范围也是不合理的。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        node = root
        res = []
        pivot = root.val
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        buf = sorted(res)
        for i in range(len(res)):
            if res[i] != buf[i]:
                return False
            if i + 1 < len(res) and buf[i] == buf[i + 1]:
                return False
        return True

    def inorder(self, node, low, high):
        if not node:
            return True
        if node.left:
            if node.left.val >= node.val:
                return False
        if node.right:
            if node.right.val <= node.val:
                return False
        if node.val <= low or node.val >= high:
            return False
        if self.inorder(node.left, low, node.val) == False:
            return False
        if self.inorder(node.right, node.val, high) == False:
            return False
        return True

    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.inorder(root, float("-inf"), float("inf"))