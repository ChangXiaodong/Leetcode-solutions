def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head:
        return False
    node = head
    while node:
        if node.val == "Nil":
            return True
        node.val = "Nil"
        node = node.next
    return False

'''
Two Point
'''
def hasCycle1(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head:
        return False
    slow = head
    fast = head.next
    while fast and fast.next and fast.next.next:
        if fast == slow:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
