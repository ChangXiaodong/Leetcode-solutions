def dfs(res, node, level):
    if not node:
        return
    if node:
        if len(res) < level + 1:
            res.append([])
        if level % 2 != 0:
            res[level].insert(0, node.val)
        else:
            res[level].append(node.val)
        dfs(res, node.left, level + 1)
        dfs(res, node.right, level + 1)


def traversal_recursive(root):
    if not root:
        return
    res = []
    dfs(res, root, 0)
    return root
