__author__ = 'Changxiaodong'
import time
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nextlevel = [root]
        if(not root):
            return 0
        depth = 0
        while(nextlevel):
            bufnode=[]
            for item in nextlevel:
                if item.left:
                    bufnode.append(item.left)
                if item.right:
                    bufnode.append(item.right)
            depth+=1
            nextlevel = bufnode
        return depth

    def nextRun(self,node):
        if node == None:
            return 0
        return max(1+self.nextRun(node.left),1+self.nextRun(node.right))


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

    test = Solution()
    start = time.clock()
    print test.maxDepth(treenode1)
    print str(time.clock() - start)
    start = time.clock()
    print test.nextRun(treenode1)
    print str(time.clock() - start)





