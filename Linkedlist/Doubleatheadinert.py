# write a code inorder to insert a element at the head and traverse the list
class Node:
    def __init__(self,data):
        self.data  = data
        self.next = None
        self.prev = None



class DoubleLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_head(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node


    def Display(self):
        current = self.head
        while current is not None:
            print(current.data,end="<-->")
            current = current.next
        print("Null")
        
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
node3.next = None

node1.prev = None
node2.prev = node1
node3.prev = node2
dll = DoubleLinkedlist()
dll.head = node1
dll.tail = node3
dll.insert_at_head(50)
dll.Display()

            
            