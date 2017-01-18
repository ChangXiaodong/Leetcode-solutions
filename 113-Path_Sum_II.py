class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pathSum1(root, sum):
    if not root:
        return []
    if root.left == None and root.right == None:
        if sum == root.val:
            return [[root.val]]
        else:
            return []
    a = pathSum1(root.left, sum - root.val) + \
        pathSum1(root.right, sum - root.val)
    return [[root.val] + i for i in a]


def pathSum(root, sum):
    if not root:
        return []
    res = []
    dfs(root, sum, [], res)
    return res


def dfs(root, sum, ls, res):
    if not root.left and not root.right and sum == root.val:
        ls.append(root.val)
        res.append(ls)
    if root.left:
        dfs(root.left, sum - root.val, ls + [root.val], res)
    if root.right:
        dfs(root.right, sum - root.val, ls + [root.val], res)


def pathSum2(root, num):
    if not root:
        return []
    res = []
    stack = [(root, num - root.val, [root.val])]
    while stack:
        curr, val, path = stack.pop()
        if not curr.left and not curr.right and val == 0:
            res.append(path)
        if curr.left:
            stack.append((curr.left, val - curr.left.val, path + [curr.left.val]))
        if curr.right:
            stack.append((curr.right, val - curr.right.val, path + [curr.right.val]))
    return res

def listAllPath(root):
    if not root:
        return []
    res = []
    stack = [(root, [root.val])]
    while stack:
        curr, path = stack.pop()
        if not curr.left and not curr.right:
            res.append(path)
        if curr.left:
            stack.append((curr.left, path + [curr.left.val]))
        if curr.right:
            stack.append((curr.right, path + [curr.right.val]))
    return res

def dfs1(node, path, res):
    if not node.left and not node.right:
        res.append(path)
    if node.left:
        dfs1(node.left, path + [node.left.val], res)
    if node.right:
        dfs1(node.right, path + [node.right.val], res)

def printAllPath(root):
    if not root:
        return []
    res = []
    dfs1(root, [root.val], res)
    return res

treenode1 = TreeNode(5)
treenode2 = TreeNode(4)
treenode3 = TreeNode(8)
treenode4 = TreeNode(11)
treenode5 = TreeNode(13)
treenode6 = TreeNode(4)
treenode7 = TreeNode(7)
treenode8 = TreeNode(2)
treenode9 = TreeNode(5)
treenode10 = TreeNode(1)

treenode1.left = treenode2
treenode1.right = treenode3
treenode2.left = treenode4
treenode3.left = treenode5
treenode3.right = treenode6
treenode4.left = treenode7
treenode4.right = treenode8
treenode6.left = treenode9
treenode6.right = treenode10

print(pathSum(treenode1, 22))
print(pathSum1(treenode1, 22))
print(pathSum2(treenode1, 22))
print(listAllPath(treenode1))
print(printAllPath(treenode1))
