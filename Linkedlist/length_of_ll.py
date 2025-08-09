"""
You are given the head of a singly linked list. Your task is to return the number of nodes in the linked list.
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
node1 = Node(10)    
node2 = Node(20)  
node3 = Node(30)  
node4 = Node(40)  
node5 = Node(50)  

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

def find_the_length(head):
    current = head
    count = 0
    while current is not None:
        count += 1
        current = current.next
    print(f"the length of linkedlist is :{count}")
    
object = find_the_length(head)