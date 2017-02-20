def find_kth(node, res):
    if node:
        find_kth(node.left)
        res.append(node.val)
        find_kth(node.right)

def find(root, k):
    res = []
    find_kth(root, res)
    return res[k]


