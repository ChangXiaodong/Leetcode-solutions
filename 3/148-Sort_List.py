# coding=utf-8
'''
归并排序
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge(self, left, right):
        if left.val < right.val:
            head = left
            left = left.next
        else:
            head = right
            right = right.next
        node = head
        while left and right:
            if left.val < right.val:
                node.next = left
                node = node.next
                left = left.next
            else:
                node.next = right
                node = node.next
                right = right.next
        while left:
            node.next = left
            node = node.next
            left = left.next
        while right:
            node.next = right
            node = node.next
            right = right.next
        return head

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        if length == 1:  #长度为1时返回
            return head
        left = head
        right = head
        for i in range(length / 2 - 1):
            right = right.next
        p = right
        right = right.next
        p.next = None
        left_sort = self.sortList(left)
        right_sort = self.sortList(right)
        return self.merge(left_sort, right_sort)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node5.next = node4
node4.next = node3
node3.next = node2
node2.next = node1
solution = Solution()
print(solution.sortList(node5))