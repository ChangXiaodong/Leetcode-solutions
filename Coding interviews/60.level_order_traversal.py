def levelorder_traversal(root):
    if not root:
        return
    nodeStack = [root]
    res = []
    while nodeStack:
        node = nodeStack.pop(0)
        if node.left:
            nodeStack.append(node.left)
        if node.right:
            nodeStack.append(node.right)
        res.append(node.val)


def dfs(res, node, level):
    if not node:
        return
    if node:
        if len(res) < level + 1:
            res.append([])
        res[level].append(node.val)
        dfs(res, node.left, level + 1)
        dfs(res, node.right, level + 1)

def level_order_traversal_recursive(root):
    if not root:
        return
    res = []
    dfs(res, root, 0)
    return root

