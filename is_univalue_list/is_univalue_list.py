class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(3)
b = Node(3)
c = Node(3)
d = Node(3)

a.next = b
b.next = c
c.next = d

def is_univalue_list(head):
    current = head
    lst = []

    while current is not None:
        lst.append(current.val)
        current = current.next
    return len(set(lst)) <= 1

print(is_univalue_list(a))        