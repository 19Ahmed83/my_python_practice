class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("a")
b = Node("b")
c = Node("f")
d = Node("g")
e = Node("h")
f = Node("r")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev    

print(reverse_list(a))    