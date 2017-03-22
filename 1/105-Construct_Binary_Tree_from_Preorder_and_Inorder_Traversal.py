'''
preorder的第一个数字为根节点，root_val
inorder中root_val之前的数字在root左子树，之后的数字在root右子树
每一次找出root_val和左子树的pre_order,ind_order右子树的pre_order,in_order，递归建树即可
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return
        root_val = preorder[0]
        root_index = inorder.index(root_val)
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]
        left_preorder = preorder[1:root_index + 1]
        right_preorder = preorder[root_index + 1:]
        node = TreeNode(root_val)
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)
        return node

