__author__ = 'Changxiaodong'
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
        try:
            print node1.val
            print node2.val
        except AttributeError,err:
            print err
        if node1 == node2 and node1 == None:
            print "True"
            return True
        elif not node1 or not node2:
            print "False1"
            return False
        elif node1.val != node2.val:
            print "Falise2"
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
    print test.isSymmetric(treenode1)
    print time.clock() - start