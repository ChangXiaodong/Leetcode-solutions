# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(start, end):
    if start > end:
        return [None]
    res = []
    for rootval in range(start, end + 1):
        LeftTree = dfs(start, rootval - 1)
        RightTree = dfs(rootval + 1, end)
        for i in LeftTree:
            for j in RightTree:
                root = TreeNode(rootval)
                root.left = i
                root.right = j
                res.append(root)
    return res


def generateTrees(n):
    if n <= 0:
        return []
    return dfs(1, n)


print(generateTrees(3))
