"""You are given the head of a singly linked list and an integer key.

Return true if the key exists in the linked list, otherwise return false.   """
class Node:
    def __init__(self,data):
        self.data  =data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

def search_element(head,key):
    current = head
    while current is not None:
        if current.data == key:
            return True
        current = current.next 
    return False
    
object = search_element(head,30)
print(object)