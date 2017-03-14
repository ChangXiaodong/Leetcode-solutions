def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    stack1 = [root]
    stack2 = []
    res = []
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)
    while stack2:
        node = stack2.pop()
        res.append(node.val)
    return res

def post_order(node, res):
    if not node:
        return
    post_order(node.left, res)
    post_order(node.right, res)
    res.append(node.val)

def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    res = []
    post_order(root, res)
    return res