#coding=utf-8
'''
getSum(node)函数计算根节点为node的子树之和
方法1：通过任意的遍历方法，遍历到每个节点时计算getSum，存在一个数组里，然后对数组进行排序，找到出现次数最多的数字。
时间复杂度O(nLogn)，因为要排序
方法2：后序遍历，遍历到中间节点时将左右子树的和累加到中心节点，然后删除左右子树。（当然不这么做也可以，删除比不删除快500ms）
将遍历结果存在一个hash map中，也就是字典。key为累加结果，value为出现次数。第一次回出现key不存在的情况，需要用字典的.get()方法。

'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def getSum(node):
    if not node:
        return 0
    return getSum(node.left) + getSum(node.right) + node.val


def findFrequentTreeSum(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    node = root
    res = []
    node_stack = []
    while node_stack or node:
        while node:
            node_stack.append(node)
            node = node.left
        node = node_stack.pop()
        res.append(getSum(node))
        node = node.right
    res.sort()
    ans = []
    count = 1
    max_count = 0
    n = res.__len__()
    i = 0
    while i < n:
        if i + count < n and res[i] == res[i + count]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                ans = []
                ans.append(res[i])
            elif count == max_count:
                ans.append(res[i])
            i = i + count
            count = 1
    return ans


def post_order(node, res):
    if not node:
        return
    post_order(node.left, res)
    post_order(node.right, res)
    get_sum = getSum(node)
    node.val = get_sum
    node.left = None
    node.right = None
    res[get_sum] = res.get(get_sum, 0) + 1


def findFrequentTreeSum1(root):
    if not root:
        return []
    hash_map = {}
    post_order(root, hash_map)
    max_num = 0
    res = []
    for i, v in hash_map.items():
        if v > max_num:
            max_num = v
            res = [i]
        elif v == max_num:
            res.append(i)
    return res


node1 = TreeNode(5)
node2 = TreeNode(2)
node3 = TreeNode(-3)
node1.left = node2
node1.right = node3

# print(findFrequentTreeSum(node1))
print(findFrequentTreeSum1(node1))
