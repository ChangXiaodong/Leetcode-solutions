__author__ = 'Changxiaodong'
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
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
        return nodeval



def dfs(node, res, level):
    if node:
        if len(res) < level + 1:
            res.append([])
        res[level].append(node.val)
        dfs(node.left, res, level + 1)
        dfs(node.right, res, level + 1)


def levelOrderTraversal(root):
    res = []
    dfs(root, res, 0)
    return res



if __name__ == "__main__":
    treenode1 = TreeNode(3)
    treenode2 = TreeNode(9)
    treenode3 = TreeNode(20)
    treenode4 = TreeNode(15)
    treenode5 = TreeNode(7)
    treenode1.left = treenode2
    treenode1.right = treenode3
    treenode3.left = treenode4
    treenode3.right = treenode5

    start = time.clock()
    test = Solution()
    print(test.levelOrderBottom(treenode1))
    print(levelOrderTraversal(treenode1))
