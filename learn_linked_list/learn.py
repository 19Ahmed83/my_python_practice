class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node("FastAPI")
second = Node("Flask")
third = Node("Django")

head.next = second
second.next = third
current = head

while current:
    print(f"[{current.data}] -> ", end="")
    current = current.next

print(None)    
