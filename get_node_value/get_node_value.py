class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("R")
b = Node("E")
c = Node("Z")
d = Node("W")

a.next = b
b.next = c
c.next = d

def get_node_value(head, index):
    current = head
    count = 0
    while current is not None:
        if count == index:
            return current.val
        current = current.next
        count += 1
    return False
print(get_node_value(a,2))    