# coding=utf-8
'''
考虑得到数字的顺序，链表是倒序的
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        count = 0
        while l1:
            num1 = num1 + l1.val * 10 ** count
            count += 1
            l1 = l1.next
        num2 = 0
        count = 0
        while l2:
            num2 = num2 + l2.val * 10 ** count
            count += 1
            l2 = l2.next
        ans = num1 + num2
        head = ListNode(ans % 10)
        node = head
        ans /= 10
        while ans > 0:
            digit = ans % 10
            ans /= 10
            node.next = ListNode(digit)
            node = node.next
        return head
