#coding=utf-8
'''
方法1：先获得两个列表长度，将长的那个列表向前移，使两个列表长度相等，然后开始逐个检查每个节点是否重合
方法2：如果不获取长度，遍历两次，nodeA先遍历A，A遍历完后再遍历B，nodeB先B后A，这样遍历的长度还是相等的。
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if not headA or not headB:
        return
    nodeA = headA
    nodeB = headB
    nodeA_num = 0
    nodeB_num = 0
    while nodeA:
        nodeA_num += 1
        nodeA = nodeA.next
    while nodeB:
        nodeB_num += 1
        nodeB = nodeB.next
    nodeA = headA
    nodeB = headB
    if nodeA_num > nodeB_num:
        for i in range(nodeA_num - nodeB_num):
            nodeA = nodeA.next
    else:
        for i in range(nodeB_num - nodeA_num):
            nodeB = nodeB.next
    while nodeA != nodeB:
        nodeA = nodeA.next
        nodeB = nodeB.next
    return nodeA

list1 = ListNode(1)
list3 = ListNode(3)
list5 = ListNode(5)
list7 = ListNode(7)
list9 = ListNode(9)
list11 = ListNode(11)
list13 = ListNode(13)
list1.next = list3
list3.next = list5
list5.next = list7
list7.next = list9
list9.next = list11
list11.next = list13
list2 = ListNode(2)
list2.next = list9
print(getIntersectionNode(list1, list2))
