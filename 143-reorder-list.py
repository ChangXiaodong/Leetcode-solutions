__author__ = 'chang'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reorderList(head):
    list_head = head
    while (head.next):
        tail = head
        while tail.next.next:
            tail = tail.next
        last_node = tail.next
        tail.next = None
        last_node.next = head.next
        head.next = last_node
        head = head.next.next
    return list_head


node0 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
# node4 = ListNode(4)
node0.next = node1
node1.next = node2
node2.next = node3
# node3.next = node4
head = reorderList(node0)
print head.val,head.next.val,head.next.next.val
