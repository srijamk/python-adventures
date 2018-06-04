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
    return l.linked_list()


def removeDupsWithoutBuffer(l):
    first_pointer = l.head
    second_pointer = first_pointer.next
    while first_pointer != second_pointer and first_pointer.next != None:

        while second_pointer != None:
            if first_pointer.value == second_pointer.value:
                l.deleteWithValue(second_pointer.value)
            second_pointer = second_pointer.next

        first_pointer = first_pointer.next
        second_pointer = first_pointer.next
    return l.linked_list()

def removeKthFromLast(k, l):
    index = len(l.linked_list()) - k
    pointer = l.head
    count = 0
    while count < len(l.linked_list()):
        if count + 1 == index:
            if pointer.next.next != None:
                pointer.next = pointer.next.next
                pointer.next.next = None
            else:
                pointer.next = None
            break
        count += 1
        
    return l.linked_list()

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
# print(removeDupsWithBuffer(l))
# print(removeDupsWithoutBuffer(l))
print(removeKthFromLast(1, l))
