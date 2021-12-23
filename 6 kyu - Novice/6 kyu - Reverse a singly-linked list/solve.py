def reverse_list(node):
    cur = node
    prev = None
    while cur:
        nextVal = cur.next
        cur.next = prev
        prev = cur
        cur = nextVal
    return prev