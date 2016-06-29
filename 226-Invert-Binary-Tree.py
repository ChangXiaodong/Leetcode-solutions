__author__ = 'Changxiaodong'
'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
import time
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def reverseTree(self,root):
        if root ==None:
            return root
        if(root.left and root.right):
            buf = root.right
            root.right = root.left
            root.left = buf
            self.invertTree(root.left)
            self.invertTree(root.right)
        elif root.left:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
        elif root.right:
            root.left = root.right
            root.right = None
            self.invertTree(root.left)

    def reverseTree1(self,root):
        if root ==None:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        self.reverseTree(root)
        return root


if __name__ == "__main__":
    treenode1 = TreeNode(1)
    treenode2 = TreeNode(2)
    treenode3 = TreeNode(3)
    # treenode1.left = treenode2
    treenode1.right = treenode3
    start = time.clock()
    test = Solution()
    node = test.invertTree(treenode1)
    # print time.clock() - start
