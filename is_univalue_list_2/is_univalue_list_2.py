class Node():
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

def is_univalue_list_2(head):
    current = head
    while current is not None:
        if current.val != head.val:
            return False
        current = current.next
    return True

print(is_univalue_list_2(a))    
        