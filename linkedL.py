

class Node:
    length = 0
    def __init__(self,data,next=None):
        self.data = data * Node.length
        self.next = next
        
# class variable
Node.length = 5
nodes = Node(5)
nodes.next = Node(20,Node(3,Node(10,Node(8))))
# Print values out
while nodes:
    print(nodes.data)
    nodes = nodes.next

# difference between instance and class
print(dir(Node))
print(dir(nodes))

