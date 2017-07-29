# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head

    def detectCycle2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        hash_table = {}
        node = head
        while node and hash_table.get(node, "null") == "null":
            hash_table[node] = 1
            node = node.next
        if hash_table.get(node, "null") != "null":
            return node
        return

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

s = Solution()
print(s.detectCycle2(node1))
