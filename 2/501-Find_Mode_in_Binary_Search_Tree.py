#coding=utf-8
'''
方法1：遍历整个树，存在hash_map中，在从hash_map中找到出现次数最多的数
方法2：中序遍历，在左子树中找出现最多的数(可以减少hashmap，space O(1)，时间复杂度一样)
'''
def findMode(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    node = root
    stack = []
    hash_map = {}
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        hash_map[node.val] = hash_map.get(node.val, 0) + 1
        node = node.right
    max_val = max(hash_map.values())
    res = []
    for key, value in hash_map.items():
        if value == max_val:
            res.append(key)
    return res