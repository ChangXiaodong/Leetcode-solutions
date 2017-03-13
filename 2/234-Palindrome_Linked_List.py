#codind=utf-8
'''
方法1：将前半部分列表反转，与后半部分对比
方法2：遍历列表存储结果，双指针头尾判断是否相等
'''
def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head:
        return True
    rev = None
    slow = head
    fast = slow
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        rev = rev.next
        slow = slow.next
    return not rev

def isPalindrome1(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head:
        return True
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    n = stack.__len__()
    for i in range(n / 2 + 1):
        if stack[i] != stack[n - 1 - i]:
            return False
    return True