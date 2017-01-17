class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root, sum):
    if not root:
        return False
    res = []
    node_buf = [root]
    while node_buf:
        node = node_buf.pop()
        if node.left:
            node.left.val += node.val
            node_buf.append(node.left)
        if node.right:
            node.right.val += node.val
            node_buf.append(node.right)
        if not node.left and not node.right:
            res.append(node.val)
    return sum in res

treenode1 = TreeNode(5)
treenode2 = TreeNode(4)
treenode3 = TreeNode(8)
treenode4 = TreeNode(11)
treenode5 = TreeNode(13)
treenode6 = TreeNode(4)
treenode7 = TreeNode(7)
treenode8 = TreeNode(2)
treenode9 = TreeNode(1)

treenode1.left = treenode2
treenode1.right = treenode3
treenode2.left = treenode4
treenode3.left = treenode5
treenode3.right = treenode6
treenode6.right = treenode9
treenode4.left = treenode7
treenode4.right = treenode8

print(hasPathSum(treenode1, 22))
