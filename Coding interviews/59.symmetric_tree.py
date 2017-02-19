def isSymmetic(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return left.val == right.val and \
           isSymmetic(left.left, right.right) and \
           isSymmetic(left.right, right.left)


def symmetric_tree(node):
    if not node:
        return
    return isSymmetic(node.left, node.right)


def symmetric_tree_recursive(node):
    if not node:
        return
    stack = [node.left, node.right]
    while stack:
        right = stack.pop()
        left = stack.pop()
        if not left and not right:
            return True
        if not left or not right:
            return False
        if right.val == left.val:
            return True
        stack.append(left.left)
        stack.append(right.right)
        stack.append(left.right)
        stack.append(right.left)
    return True
