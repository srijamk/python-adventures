class Queue():
    """
    Creates a representation of a Queue, a First-In-First-Out, linear, sequential
    data structure.

    isEmpty(): Returns a boolean representing whether the queue is empty or not
    peek(): Returns the first element in the queue
    add(value): Adds a new element to the end of the queue
    remove(): Removes and returns the first element in the queue
    
    """
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[0]

    def add(self, value):
        self.queue.append(value)

    def remove(self):
        first_in = self.queue[0]
        self.queue.remove(first_in)
        return first_in

q = Queue()
print(q.isEmpty())
q.add("Adam")
q.add("Bob")
q.add("Chad")
q.remove()
print(q.peek())
q.remove()
print(q.queue)
