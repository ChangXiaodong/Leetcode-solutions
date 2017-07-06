# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reorderList(head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """
    list_node_stack = []
    head_pointer1 = head
    head_pointer2 = head
    while head_pointer2:
        list_node_stack.append(head_pointer2)
        head_pointer2 = head_pointer2.next
    length = len(list_node_stack)
    if length < 3:
        return
    list_node_stack = list_node_stack[length / 2:]
    for i in range(length / 2):
        listnode = list_node_stack.pop()
        listnode.next = head_pointer1.next
        head_pointer1.next = listnode
        head_pointer1 = head_pointer1.next.next
    head_pointer1.next = None
    return head


# Splits in place a list in two halves, the first half is >= in size than the second.
# @return A tuple containing the heads of the two halves
def _splitList(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        fast = fast.next

    middle = slow.next
    slow.next = None

    return head, middle


# Reverses in place a list.
# @return Returns the head of the new reversed list
def _reverseList(head):
    last = None
    currentNode = head

    while currentNode:
        nextNode = currentNode.next
        currentNode.next = last
        last = currentNode
        currentNode = nextNode

    return last


# Merges in place two lists
# @return The newly merged list.
def _mergeLists(a, b):
    tail = a
    head = a

    a = a.next
    while b:
        tail.next = b
        tail = tail.next
        b = b.next
        if a:
            a, b = b, a

    return head


class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return

        a, b = _splitList(head)
        b = _reverseList(b)
        head = _mergeLists(a, b)


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# head = reorderList(node1)
middle1 = split_list(node1)
while middle1:
    print(middle1.val)
    middle1 = middle1.next
print('---------')
middle2 = _splitList(node1)
while middle2:
    print(middle2.val)
    middle2 = middle2.next
