# write a code of double linkedlist jidar aap 
# head ko aur tail of linkedlist ko delte kare ho theek hian
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class Doublelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def adding_at_element(self,val):
        new_node  = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            return 
        new_node.next = self.head
        self.head.prev = new_node 
        self.head = new_node
        
        
        
    def delete_at_head(self):
        if not self.head:                        # empty list 
            print("list is empty ")
            return 
        if self.head == self.tail:               # single node 
            self.head = self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None
       
        
    def delete_at_tail(self):
        if not self.tail:
            print("list is empty ")
            return
        if self.head == self.tail :
            self.head = self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None
       
        
    def delete_at_specific(self,index):
        if not self.head:
            print("list is empty ")
            return
        # traverse the list 
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        
        # if position
        if current == self.head:
            self.delete_at_head()
            return 
        
        #if position is tail
        if current == self.tail:
            self.delete_at_tail()
            return 
        # current is out of bound
        if not current:
            print(" out of bound ")
            return 
        # middle values ke position
        current.prev.next = current.next
        current.next.prev = current.prev
        
    def Display(self):
        current = self.head
        while current :
            print(current.data,end="<-->")
            current = current.next
        print("Null")
        
dll = Doublelinkedlist()

print("adding the element in the list ")
dll.adding_at_element(30)
dll.adding_at_element(20)
dll.adding_at_element(10)

print(" the double linked list is ")
dll.Display()


# ## edar yeh at deleting at head ka hain 

print("before  deleting the head ")
dll.Display()
dll.delete_at_head()
print("after deleting the head")
dll.Display()


# edar yeh at deleting at tail  ka hain 

print("before deleting the tail")
dll.Display()
dll.delete_at_tail()
print("after deleting the tail :")
dll.Display()

# edar yeh at specific position ka hain 

print("before deleting the node at specific index = 2:")
dll.Display()
dll.delete_at_specific(2)
print("after deleting the node at specific position of index 2 is :")
dll.Display()



        
        
        
       