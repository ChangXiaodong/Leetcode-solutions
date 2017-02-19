def entry_node(node):
    if not node:
        return
    p1 = node
    p2 = node
    while p1.val != p2.val:
        p1 = p1.next
        p2 = p2.next.next
    cur_val = p1.val
    loop_count = 0
    p1 = p1.next
    while p1.val != cur_val:
        p1 = p1.next
        loop_count += 1
    p1 = node
    p2 = node
    for i in range(loop_count):
        p1 = p1.next
    while p1.val != p2.val:
        p1 = p1.next
        p2 = p2.next
    return p1
