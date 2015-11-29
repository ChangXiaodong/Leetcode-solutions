__author__ = 'Changxiaodong'
import time


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodeval = []
        levelval = []
        levelnode = []
        bufnode = []
        if not root:
            return []
        levelnode.append(root)
        while levelnode:
            for node in levelnode:
                levelval.append(node.val)
                if node.left:
                    bufnode.append(node.left)
                if node.right:
                    bufnode.append(node.right)
            levelnode = bufnode
            bufnode = []
            nodeval.append(levelval)
            levelval = []
        nodeval.reverse()
        return nodeval


if __name__ == "__main__":
    treenode1 = TreeNode(1)
    treenode2 = TreeNode(2)
    treenode1.left = treenode2

    start = time.clock()
    test = Solution()
    print test.levelOrderBottom(treenode1)
    print time.clock() - start
