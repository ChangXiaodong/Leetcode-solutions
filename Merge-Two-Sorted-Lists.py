__author__ = 'Changxiaodong'
import time


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l3.val = l1.val
            head = l3
            l1 = l1.next
        elif l1.val > l2.val:
            l3.val = l2.val
            head = l3
            l2 = l2.next
        else:
            l3.val = l1.val
            head = l3
            l3.next = l2
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        while l1 and l2:
            if l1.val < l2.val:
                l3.next = ListNode(0)
                l3.next.val = l1.val
                l3 = l3.next
                l1 = l1.next
            elif l1.val > l2.val:
                l3.next = ListNode(0)
                l3.next.val = l2.val
                l3 = l3.next
                l2 = l2.next
            else:
                l3.next = ListNode(0)
                l3.next.val = l1.val
                l3 = l3.next
                l3.next = ListNode(0)
                l3.next.val = l2.val
                l3 = l3.next
                l1 = l1.next
                l2 = l2.next
        if not l1:
            l3.next = l2
        if not l2:
            l3.next = l1
        return head


if __name__ == "__main__":
    start = time.clock()

    l1 = ListNode(-9)
    l1.next = ListNode(-7)
    l1.next.next = ListNode(-3)
    l1.next.next.next = ListNode(-3)
    l1.next.next.next.next = ListNode(-1)
    l1.next.next.next.next.next = ListNode(2)
    l1.next.next.next.next.next.next = ListNode(3)
    l2 = ListNode(-7)
    l2.next = ListNode(-7)
    l2.next.next = ListNode(-6)
    l2.next.next.next = ListNode(-6)
    l2.next.next.next.next = ListNode(-5)
    l2.next.next.next.next.next = ListNode(-3)
    l2.next.next.next.next.next.next = ListNode(2)
    l2.next.next.next.next.next.next.next = ListNode(4)
    test = Solution()
    l3 = test.mergeTwoLists(l1, l2)
    while(l3):
        print l3.val
        l3 = l3.next

    print time.clock() - start
