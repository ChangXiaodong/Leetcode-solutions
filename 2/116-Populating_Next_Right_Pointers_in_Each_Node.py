'''
方法1：按层次遍历，按遍历顺序把每个节点连接起来
方法2：有一个指针一直在左子树，另一个指针查找。对着程度connect1看过程就能看懂。
'''
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        stack1 = [root]
        stack2 = []
        while 1:
            if stack1:
                last_node = stack1.pop(0)
                if last_node.left:
                    stack2.append(last_node.left)
                if last_node.right:
                    stack2.append(last_node.right)
            while stack1:
                node = stack1.pop(0)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
                last_node.next = node
                last_node = node
            last_node.next = None
            if not stack2:
                break
            stack1[:] = stack2[:]
            stack2 = []

    def connect1(self, root):
        if not root:
            return
        pre = root
        while pre.left:
            node = pre
            while node.next:
                node.left.next = node.right
                node.right.next = node.next.left
                node = node.next
            node.left.next = node.right
            node.next = None
            pre = pre.left





