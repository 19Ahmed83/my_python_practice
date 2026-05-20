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

def qty_of_nodes(root):
    if root is None:
        return 0
    stack = [root]
    total = 0

    while stack:
        node = stack.pop()
        total += 1

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return total 

if __name__ == "__main__":
    result = qty_of_nodes(a)
print(result) 

#        a
#      /   \
#     b     c
#    / \   /  
#   d   e f
# 6
