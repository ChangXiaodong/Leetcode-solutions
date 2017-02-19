def next_node(node):
    if not node:
        return
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    while node.parent and node.parent.right.val == node.val:
        node = node.parent
        return node.parent


