__author__ = 'Changxiaodong'
'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''
import time
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p is None and q is None):
            return True
        elif p and q:
            return (p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        else:
            return False
if __name__ == "__main__":
    treenode1 = TreeNode(1)
    treenode2 = TreeNode(2)
    treenode3 = TreeNode(3)
    treenode4 = TreeNode(4)
    treenode5 = TreeNode(5)
    treenode6 = TreeNode(6)
    treenode7 = TreeNode(7)
    treenode8 = TreeNode(8)
    treenode9 = TreeNode(9)
    treenode10 = TreeNode(10)
    treenode11 = TreeNode(11)
    treenode1.left = treenode2
    treenode1.right = treenode3
    treenode2.left = treenode4
    treenode2.right = treenode5
    treenode3.left = treenode6
    treenode3.right = treenode7
    treenode4.left = treenode8
    treenode8.left = treenode9
    treenode9.right = treenode10
    start = time.clock()
    test = Solution()
    print test.isSameTree(treenode8,treenode9)

    print time.clock() - start
