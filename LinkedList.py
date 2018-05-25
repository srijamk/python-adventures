class Node():
    
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None
        self.count = 0

    def length(self):
        return self.count

    def append(self, value):
        self.count += 1
        if self.head == None:
            self.head = Node(value)
            return
        
        current = self.head
        while current.next != None:
            current = this.next
        current.next = Node(value)
        
    def prepend(self, value):
        self.count += 1
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def deleteWithValue(self, value):
        self.count -= 1
        if self.head == None:
            return

        current = self.head
        print(self.head.value)
        while current.next != None:
            if current.next.value == value:
                current.next = current.next.next
            current = current.next
