class Node():
    def __init__(self,val):
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

def breadth_first_values(root):
    if not root:
        return []
    queue = [root]
    values = []
    
    while queue:
        current = queue.pop(0)
        values.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)    
        

    return values 
if __name__ == "__main__":
    print(breadth_first_values(a))

#        a
#      /   \
#     b     c
#    / \   /
#   d   e f 
# 
# ["a", "b", "c", "d", "e", "f"]
#     