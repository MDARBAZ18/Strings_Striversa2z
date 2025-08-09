""" 
Given the head of a singly linked list and an integer X, insert a node with value X at the head of the linked list and return the head of the modified list.



The head is the first node of the linked list.
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
head = node1
node1.next = node2
node2.next = node3
node3.next = None

def Insert_at_head(head,X):
    new_node = Node(X)
    new_node.next = head
    head = new_node
    print(head.data)
    return head
    
    

def Display(head):
    current = head
    while current is not None:
        print(current.data,end="->")
        current = current.next 
    print("NULL")


object = Insert_at_head(head,50)
Display(object)
