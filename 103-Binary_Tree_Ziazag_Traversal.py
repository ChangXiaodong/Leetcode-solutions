class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    if not root:
        return []

    traversal = []
    level_buf = []
    level_node_buf = []

    level_node_buf.append(root)
    while level_node_buf:
        next_level_node_buf = []
        for node in level_node_buf:
            level_buf.append(node.val)
            if node.left:
                next_level_node_buf.append(node.left)
            if node.right:
                next_level_node_buf.append(node.right)

        level_node_buf = next_level_node_buf
        traversal.append(level_buf)
        level_buf = []
    for i, v in enumerate(traversal):
        if i % 2 != 0:
            traversal[i] = traversal[i][::-1]
    return traversal


# dfs recursive
def dfs(node, res, level):
    if node:
        if len(res) < level + 1:
            res.append([])
        if level % 2 == 0:
            res[level].append(node.val)
        else:
            res[level].insert(0, node.val)
        dfs(node.left, res, level + 1)
        dfs(node.right, res, level + 1)

def zigzagLevelOrder1(root):
    res = []
    dfs(root, res, 0)
    # dfs1(root, 0, res)
    return res


treenode1 = TreeNode(1)
treenode2 = TreeNode(2)
treenode3 = TreeNode(3)
treenode4 = TreeNode(4)
treenode5 = TreeNode(5)
treenode1.left = treenode2
treenode1.right = treenode3
treenode2.left = treenode4
treenode3.right = treenode5

print(zigzagLevelOrder(treenode1))
print(zigzagLevelOrder1(treenode1))
