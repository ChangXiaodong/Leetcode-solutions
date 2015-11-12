__author__ = 'Changxiaodong'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        node_buf = [None]
        while(node):
            node_buf.append(node)
            node = node.next
        head_node = node_buf.pop()
        node = head_node
        while(node):
            node.next = node_buf.pop()
            node = node.next
        return head_node