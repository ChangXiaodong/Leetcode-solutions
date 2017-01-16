def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    depth = 0
    node = root
    traversal = []
    while node:
        if depth % 2 == 0: