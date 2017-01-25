
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder_traversal_recursive(root, res):
    if not root:
        return
    res.append(root.val)
    if root.left:
        preorder_traversal_recursive(root.left, res)
    if root.right:
        preorder_traversal_recursive(root.right, res)


def preorder_traversal(root):

    if not root:
        return
    node_buf = []
    node = root
    res = []
    while node or node_buf:
        while node:
            res.append(node.val)
            node_buf.append(node)
            node = node.left
        node = node_buf.pop()
        node = node.right
    return res


def inorder_traversal(root):
    if not root:
        return
    node_buf = []
    node = root
    res = []
    while node or node_buf:
        while node:
            node_buf.append(node)
            node = node.left
        node = node_buf.pop()
        res.append(node.val)
        node = node.right
    return res



def postorder_traversal(root):
    if not root:
        return
    node_buf1 = []
    node_buf2 = []
    res = []
    node = root
    node_buf1.append(node)
    while node_buf1:
        node = node_buf1.pop()
        if node.left:
            node_buf1.append(node.left)
        if node.right:
            node_buf1.append(node.right)
        node_buf2.append(node)
    while node_buf2:
        node = node_buf2.pop()
        res.append(node.val)
    return res


def inorder_traversal_recursive(root, res):
    if not root:
        return
    if root.left:
        inorder_traversal_recursive(root.left, res)
    res.append(root.val)
    if root.right:
        inorder_traversal_recursive(root.right, res)


def level_traversal(root):
    if not root:
        return
    node_stack = []
    node_stack.append(root)
    res = []
    while node_stack:
        node = node_stack.pop(0)
        res.append(node.val)
        if node.left:
            node_stack.append(node.left)
        if node.right:
            node_stack.append(node.right)
    return res


def postorder_traversal_recursive(root, res):
    if not root:
        return
    if root.left:
        postorder_traversal_recursive(root.left, res)
    if root.right:
        postorder_traversal_recursive(root.right, res)
    res.append(root.val)


def traversal(root):
    pre_order = []
    in_order = []
    post_order = []
    preorder_traversal_recursive(root, pre_order)
    inorder_traversal_recursive(root, in_order)
    postorder_traversal_recursive(root, post_order)
    print("pre order:{}".format(pre_order))
    print(preorder_traversal(treeode1))
    print("in order:{}".format(in_order))
    print(inorder_traversal(treeode1))
    print("post order:{}".format(post_order))
    print(postorder_traversal(treeode1))




treeode1 = TreeNode("0")
treeode2 = TreeNode("1")
treeode3 = TreeNode("2")
treeode4 = TreeNode("3")
treeode5 = TreeNode("4")
treeode6 = TreeNode("5")
treeode7 = TreeNode("6")
treeode8 = TreeNode("7")
treeode9 = TreeNode("8")
treeode10 = TreeNode("9")

treeode1.left = treeode2
treeode1.right = treeode3
treeode2.left = treeode4
treeode2.right = treeode5
treeode3.right = treeode6
treeode4.left = treeode8
treeode4.right = treeode9
treeode5.left = treeode10
treeode3.left = treeode6
treeode3.right = treeode7

traversal(treeode1)
print("level traversal{}".format(level_traversal(treeode1)))
