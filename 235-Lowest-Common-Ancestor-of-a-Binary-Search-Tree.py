__author__ = 'Changxiaodong'
'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
'''
import time
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def isLowest(self,root,p,q):
        self.node = root
        if root.val > max(p.val,q.val):
            self.isLowest(root.left,p,q)
        if root.val < min(p.val,q.val):
            self.isLowest(root.right,p,q)
        return root

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.node = root
        self.isLowest(root,p,q)
        return self.node


if __name__ == "__main__":
    treenode1 = TreeNode(1)
    treenode2 = TreeNode(2)
    treenode3 = TreeNode(3)
    treenode4 = TreeNode(4)
    treenode5 = TreeNode(5)
    treenode6 = TreeNode(6)
    treenode5.left = treenode3
    treenode5.right = treenode6
    treenode3.left = treenode2
    treenode3.right = treenode4
    treenode2.left = treenode1
    start = time.clock()
    test = Solution()
    print test.lowestCommonAncestor(treenode5,treenode1,treenode4).val
    print time.clock() - start
