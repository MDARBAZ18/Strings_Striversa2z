"""
Given the head of a singly linked list, delete the head of the linked list and return the head of the modified list.
The head is the first node of the linked list.
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#adding the nodes at the linkedlist
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# connecting between the linkedlist
head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

def Deleting_at_head(head):
    if head is None:
        return None
    deleted_node = head.data
    print(f"the head which is delted is : {deleted_node}")
    head = head.next
    return head
   
def Display(head):
    current = head
    while current is not None:
        print(current.data,end="->")
        current = current.next
    print("Null")
    
object = Deleting_at_head(head)
Display(object)
