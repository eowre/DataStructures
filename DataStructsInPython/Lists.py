class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        
class Node2:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        
class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        
def SLL():
    linked_list = LinkedList()
    
    #creating Nodes
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    linked_list.head.next = second
    second.next = third
    
    print("priting singly linked list in order")
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next
    print("\n")

def DLL():
    doubly_linked_list = DoublyLinkedList
    
    doubly_linked_list.head = Node2(1)
    second = Node2(2)
    third = Node2(3)
    doubly_linked_list.tail = Node2(4)
    
    doubly_linked_list.head.next = second
    second.prev = doubly_linked_list.head
    second.next = third
    third.prev = second
    third.next = doubly_linked_list.tail
    doubly_linked_list.tail.prev = third
    
    print("printing DLL head to tail")    
    while doubly_linked_list.head != None:
        print(doubly_linked_list.head.item, end=" ")
        doubly_linked_list.head = doubly_linked_list.head.next
    print("\n")
    
    print("Printing DLL tail to head")    
    while doubly_linked_list.tail != None:
        print(doubly_linked_list.tail.item, end=" ")
        doubly_linked_list.tail = doubly_linked_list.tail.prev
    print("\n")
    
    #NOTE: can use this doubly linked list to create a cyclicly linked list
    

def main():
    SLL()
    DLL()

    
        
if __name__ == '__main__':
    main()
    