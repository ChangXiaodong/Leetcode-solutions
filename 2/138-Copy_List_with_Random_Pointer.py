# coding=utf-8
'''
方法1：用一个队列存储random，先复制主list然后复制randomlist
方法2：直接点每个节点后复制，然后把奇数偶数的list拆分出来
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        stack = []
        if not head:
            return
        new_head = RandomListNode(head.label)
        new_node = new_head
        node = head
        while node.next:
            new_node.next = RandomListNode(node.next.label)
            stack.append(node.random)
            node = node.next
            new_node = new_node.next
        stack.append(node.random)
        new_node = new_head
        while stack:
            random_node = stack.pop(0)
            if random_node:
                new_node.random = RandomListNode(random_node.label)
            new_node = new_node.next
        return new_head
