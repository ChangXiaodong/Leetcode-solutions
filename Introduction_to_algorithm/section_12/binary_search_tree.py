class TreeNode(object):
    def __int__(self, val):
        self.p = None
        self.key = val
        self.left = None
        self.right = None


def recursive_tree_search(tree_node, key):
    if tree_node is None or key == tree_node.key:
        return tree_node
    if key < tree_node.key:
        return recursive_tree_search(tree_node.left, key)
    else:
        return recursive_tree_search(tree_node.right, key)


def iterative_tree_search(tree_node, key):
    while tree_node and key != tree_node.key:
        if key < tree_node.key:
            tree_node = tree_node.left
        else:
            tree_node = tree_node.right
    return tree_node


def tree_minimum(node):
    while node.left:
        node = node.left
    return node


def tree_maximum(node):
    while node.right:
        node = node.right
    return node


def tree_successor(node):
    if node.right:
        return tree_minimum(node.right)
    y = node.p
    while y and y.right == node:
        node = y
        y = y.p
    return y


def tree_insert(root, node):
    x = root
    while x:
        y = x
        if node.key < x.key:
            x = x.left
        else:
            x = x.right
    node.p = y
    if y is None:
        root = node
    elif node.key < y.key:
        y.left = node
    else:
        y.right = node
    return root


def transplant(root, before, after):
    if before.p is None:
        root = after
    elif before == before.p.left:
        before.p.left = after
    else:
        before.p.right = after
    if after:
        after.p = before.p
    return root


def tree_delete(root, node):
    if node.left is None:
        transplant(root, node, node.right)
    elif node.right is None:
        transplant(root, node, node.left)
    else:
        y = tree_minimum(node.right)
        if y.p != node:
            # y.p.right = y.right
            # y.right.p = y.p
            transplant(root, y, y.right)
            y.right = node.right
            y.right.p = y
        transplant(root, node, y)
        y.left = node.left
        y.left.p = y
    return root
