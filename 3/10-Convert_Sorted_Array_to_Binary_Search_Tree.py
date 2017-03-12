# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    n = nums.__len__()
    if not nums:
        return
    half = n // 2
    root = TreeNode(nums[half])
    root.left = sortedArrayToBST(nums[:half])
    root.right = sortedArrayToBST(nums[half + 1:])
    return root