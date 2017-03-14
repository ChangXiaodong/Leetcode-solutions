def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    stack = []
    node = root
    res = []
    while node or stack:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return res

def pre_order( node, res):
    if not node:
        return
    res.append(node.val)
    pre_order(node.left, res)
    pre_order(node.right, res)

def preorderTraversal1(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    res = []
    pre_order(root, res)
    return res