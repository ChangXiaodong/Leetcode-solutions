# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def dfs(self, node, path, table):
        if not node:
            return
        path.append(node.val)
        table[node.val] = path[:]
        if node.left:
            self.dfs(node.left, path, table)
            path.pop()
        if node.right:
            self.dfs(node.right, path, table)
            path.pop()

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        table = {}
        self.dfs(root, [], table)
        for n in table[p.val][::-1]:
            for m in table[q.val][::-1]:
                if n == m:
                    return m


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node2
node1.right = node3
node2.right = node4
solution = Solution()
print(solution.lowestCommonAncestor(node1, node3, node4))
