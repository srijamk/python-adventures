class Node:
    """
    Creates a representation of a Node, which is a single element in the Linked List. Each Node instance has a value and a reference 
    pointing to another Node.
    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

class LinkedList:
    """
    Creates a representation of a Linked List, a linear data structure without a physical sequential order. It is composed of nodes (elements) 
    that have both a value and a reference, the latter pointing to another element.
    
    length(): Returns an integer length of the linked list
    append(value): Adds value to the end of the linked list, setting the current last node's reference to the new value
    prepend(value): Adds value to the start of the linked list, setting its reference to the current first node
    deleteWithValue(value): Deletes value from the linked list
    
    """
    
    def __init__(self):
        self.head = None
        self.count = 0
        self.linkedlist = []

    def length(self):
        return self.count

    def append(self, value):
        self.linkedlist.append(value)
        self.count += 1
        if self.head == None:
            self.head = Node(value)
            return

        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(value)

    def prepend(self, value):
        self.linkedlist.insert(0, value)
        self.count += 1
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def deleteWithValue(self, value):
        self.linkedlist.remove(value)
        self.count -= 1
        if self.head == None:
            return

        current = self.head
        while current.next != None:
            if current.next.value == value:
                current.next = current.next.next
            current = current.next

#a = LinkedList()
#a.append(1)
#a.append(2)
#a.prepend(3)
#a.deleteWithValue(3)
#print(a.head.value)
#a.deleteWithValue(1)
#print(a.head.value)
