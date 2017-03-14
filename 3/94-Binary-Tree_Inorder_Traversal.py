def inorderTraversal(root):
    if not root:
        return []
    stack = []
    node = root
    res = []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node.pop()
        res.append(node.val)
        node = node.right
    return res

def visit_node(node, res):
    if not node:
        return
    visit_node(node.left, res)
    res.append(node.val)
    visit_node(node.right, res)

def inorder_recursive(root):
    if not root:
        return []
    res = []
    visit_node(root, res)
    return res