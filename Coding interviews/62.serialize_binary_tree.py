class Tree_node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TreeNode(object):
    def __init__(self):
        self.lChild = None
        self.rChild = None


def serialize(node):
    if not node:
        print("$")
        return
    print("{},".format(node.val))
    serialize(node.left)
    serialize(node.right)


def deserialize(node_list, node):
    if node_list and node_list[0] != '$':
        root = Tree_node(node_list.pop(0))
        node.left = root
        deserialize(node_list, node.left)
    if node_list and node_list[0] != '$':
        root = Tree_node(node_list.pop(0))
        node.right = root
        deserialize(node_list, node.right)
    if node and node_list[0] == '$':
        node_list.pop(0)


def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)


arr = [1, 2, 4, '$', '$', '$', 3, 5, '$', '$', 6, '$', '$']
root = Tree_node(arr[0])
deserialize(arr, root)

print_tree(root)
