# write a code for inserting the nodes at 3 specific places 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class dll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def adding_element(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
        
    def insert_at_head(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def insert_at_tail(self,val):
        new_node = Node(val)
        if not self.tail :
            self.head = self.tail = new_node
            return
        self.tail.next = new_node 
        new_node.next = None
        self.tail = new_node
        
    def insert_at_specific(self,index,val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            return 
        current  = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
            
        if current == self.head:
            self.insert_at_head(val)
            return
        
        if current == self.tail:
            self.insert_at_tail(val)
            return
        if not current:
            print(" the element is out of bound bas ")
        # if we have to add at the middle then this logic is applied    
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        
    def Display(self):
        current = self.head
        while current :
            print(current.data,end="<-->")
            current = current.next
        print("Null")
        
dll = dll()

print("linkedlist is empty ryt now , lets add using adding method")

dll.adding_element(30)
dll.adding_element(20)
dll.adding_element(10)
print("after adding the elements in the list here the dobule linkedlist")
dll.Display()

# inserting at the head value
print("before adding the node at head")
dll.Display()
dll.insert_at_head(40)
print("after adding the element at the head")
dll.Display()

# # inserting at specific position 
print("before adding the element at specific place")
dll.Display()
dll.insert_at_specific(2,50)
print("after adding the element at specific positon ")
dll.Display()

# inserting element at tail
print("before inserting at tail :")
dll.Display()
dll.insert_at_tail(60)
print("after adding the element at tail :")
dll.Display()


            
        
            
        
        