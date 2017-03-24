'''
方法1：用dfs方法遍历树，记录下从root到p和从root到q的路径，比较路径中最靠后的相同节点。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def dfs(self, node, path, table, p, q):
        if not node:
            return
        path.append(node.val)
        if node == p:
            table[0] = path[:]
        elif node == q:
            table[1] = path[:]
        if node.left:
            self.dfs(node.left, path, table, p, q)
            path.pop()
        if node.right:
            self.dfs(node.right, path, table, p, q)
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
        table = [[], []]
        self.dfs(root, [], table, p, q)
        for n in table[0][::-1]:
            for m in table[1][::-1]:
                if n == m:
                    return m

    def lowestCommonAncestor1(self, root, p, q):
        #如果root为空，则说明没有找到p，q返回空
        #如果root等于p或q。说明找到，返回root
        if root in (None, p, q):
            return root
        #在左子树中查找p，q
        left = self.lowestCommonAncestor1(root.left, p, q)
        #在右子树中查找p，q
        right = self.lowestCommonAncestor1(root.right, p, q)
        #如果左子树和右子树都找到了，说明该节点就是LCA
        if left and right:
            return root

        return left if left else right


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node2
node1.right = node3
node2.right = node4
solution = Solution()
print(solution.lowestCommonAncestor(node1, node3, node4))
