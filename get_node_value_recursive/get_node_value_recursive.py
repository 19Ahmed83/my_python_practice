class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("E") 
b = Node("G")
c = Node("P")
d = Node("Y")

a.next = b
b.next =c
c.next = d

def get_node_value_recursive(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    
    return get_node_value_recursive(head.next, index - 1)

print(get_node_value_recursive(a, 2))
    
