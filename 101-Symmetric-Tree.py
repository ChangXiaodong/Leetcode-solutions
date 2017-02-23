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
        return self.isSym(root.left,root.right)

    def isSym(self,node1,node2):
        if node1 == node2 and node1 == None:
            return True
        elif not node1 or not node2:
            return False
        elif node1.val != node2.val:
            return False

        return self.isSym(node1.left,node2.right) and self.isSym(node1.right,node2.left)


if __name__ == "__main__":
    treenode1 = TreeNode(1)
    treenode2 = TreeNode(2)
    treenode3 = TreeNode(2)
    treenode1.left = treenode2
    treenode1.right = treenode3
    start = time.clock()
    test = Solution()
    test.isSymmetric(treenode1)