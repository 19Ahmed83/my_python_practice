class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def tree_sum(root):
    if root is None:
        return 0
    stack = [root]
    total = 0

    while stack:
        node = stack.pop()
        total += node.val

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return total            


if __name__ == "__main__":
    result = tree_sum(a)
print(result)

#          3
#        /   \
#      11     4
#     /  \   /
#    4   -2 1
#
#  21






