class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def depth_first_values(root):
    if not root:
        return []
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)

    return [root.val, *left_values, *right_values]


print(depth_first_values(a))            