__author__ = 'Changxiaodong'
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''
import time


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSym(root.left, root.right)

    def isSym(self, node1, node2):
        if node1 == node2 and node1 == None:
            return True
        elif not node1 or not node2:
            return False
        elif node1.val != node2.val:
            return False

        return self.isSym(node1.left, node2.right) and self.isSym(node1.right, node2.left)

    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [root.left, root.right]
        while stack:
            right = stack.pop()
            left = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True


if __name__ == "__main__":
    tree1 = TreeNode(2)
    tree2 = TreeNode(3)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(5)
    tree1.left = tree2
    tree1.right = tree3
    tree2.left = tree4
    tree2.right = tree5
    tree3.left = tree6
    s = Solution()
    print(s.isSymmetric1(tree1))