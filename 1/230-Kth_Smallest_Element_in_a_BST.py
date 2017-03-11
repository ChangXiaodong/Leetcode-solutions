def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    node_stack = []
    level = 0
    node = root
    while node or node_stack:
        while node:
            node_stack.append(node)
            node = node.left
        node = node_stack.pop()
        level += 1
        if level == k:
            return node.val
        node = node.right