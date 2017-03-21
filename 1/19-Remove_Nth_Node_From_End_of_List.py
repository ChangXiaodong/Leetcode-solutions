'''
双指针，point1指针先走n步。然后poin1,point2同时后移，当point1为None时，point2为要删除的节点。
注意n==链表长度的情况
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return
        point1 = head
        point2 = head
        for i in range(n):
            point1 = point1.next
        if point1 is None:
            head = head.next
            return head
        while point1:
            last_node = point2
            point1 = point1.next
            point2 = point2.next
        last_node.next = point2.next
        return head