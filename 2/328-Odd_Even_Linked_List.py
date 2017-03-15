#coding=utf-8
'''
注意链表为1时的处理
注意指针更新的条件，在纸上能够推理出结果。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return
    odd = head
    even = head.next
    even_head = even
    buf = None
    while even and even.next:
        buf = even.next
        even.next = even.next.next
        even = even.next
        odd.next = buf
        odd = buf
    if buf:
        buf.next = even_head
    return head

list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(4)
list5 = ListNode(5)
list6 = ListNode(6)
list7 = ListNode(7)
list8 = ListNode(8)
list9 = ListNode(9)
list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5
list5.next = list6
list6.next = list7
list7.next = list8

print(oddEvenList(list1))
