class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

def remove_node(head, target_val):
    if head.val == target_val:
        return head.next
    
    current = head
    prev = None

    while current is not None:
        if current.val == target_val:
            prev.next = current.next
            break
        prev = current
        current = current.next

    return head

print(remove_node(a, "c"))    