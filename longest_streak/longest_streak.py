class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node(3)
b = Node(3)
c = Node(5)
d = Node(5)
e = Node(5)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

def longest_streak(head):
    current_node = head
    max_streak = 0
    current_streak = 0
    prev_val = None

    while current_node is not None:
        if current_node.val == prev_val:
            current_streak += 1
        else:
            current_streak = 1

        prev_val = current_node.val

        if current_streak > max_streak:
            max_streak = current_streak

        current_node = current_node.next

    return max_streak

print(longest_streak(a))                