class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("A")
b = Node("F")
c = Node("G")
d = Node("T")

a.next = b
b.next = c
c.next = d

def linked_list_find(head,target):
    current = head
    while current is not None:
        if current.val == target:
            return True
        current = current.next
    return False
            
print(linked_list_find(a, "G"))            