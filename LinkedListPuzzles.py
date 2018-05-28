from LinkedList import LinkedList
from LinkedList import Node

def removeDupsWithBuffer(l):
    if l.head.next == None:
        return l

    buffer = []
    head = l.head
    while head != None:
        if head.value not in buffer:
            buffer.append(head.value)
        else:
            l.deleteWithValue(head.value)
        head = head.next
    return l.linkedlist

def removeDupsWithoutBuffer(l):
    print(len(l.linkedlist))
    first_pointer = l.head
    second_pointer = first_pointer.next
    while first_pointer != second_pointer:
        
        while second_pointer != None:
           
            if first_pointer.value == second_pointer.value:
                print("hi")
                l.deleteWithValue(second_pointer)
            print(first_pointer.value, first_pointer.next.value, first_pointer.next.next.value)
            second_pointer = second_pointer.next
            #print(first_pointer.value, second_pointer.value)
        first_pointer = first_pointer.next
        second_pointer = first_pointer
    return l.linkedlist

l = LinkedList()
l.append(1)
l.append(2)
l.append(2)
#print(removeDupsWithBuffer(l))
print(removeDupsWithoutBuffer(l))
