class Node(object):
    def __init__(self, val):
        self.next = None
        self.val = val


def delete_node(node):
    if not node:
        return

    p1 = node
    p2 = node.next
    delete_flag = 0
    while p2.next:
        if p2.val != p2.next.val:
            if p2.next.val == p2.next.next.val:
                p2 = p2.next
                if delete_flag == 0:
                    p1 = p1.next
                continue
            if delete_flag == 1:
                delete_flag = 0
                p1.next = p2.next
            p1 = p1.next
            p2 = p2.next
        else:
            delete_flag = 1
            p2 = p2.next
    if delete_flag == 1:
        p1.next = None
        return node
    return node


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node33 = Node(3)
node333 = Node(3)
node4 = Node(4)
node44 = Node(4)
node444 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node33
# node33.next = node333
# node333.next = node4
# node4.next = node44
# node44.next = node444

node = delete_node(node1)
while node:
    print(node.val)
    node = node.next
