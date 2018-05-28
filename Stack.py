class Stack():
    """
    Creates a representation of a Stack, a Last-In-First-Out, linear, sequential
    data structure.

    isEmpty(): Returns a boolean representing whether the stack is empty or not
    peek(): Returns the top element in the stack
    add(value): Adds a new element to the end of the stack
    remove(): Removes and returns the top element in the stack
    
    """
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        last_in = self.stack[-1]
        self.stack.remove(last_in)
        return last_in

s = Stack()
print(s.isEmpty())
s.push("Adam")
s.push("Bob")
s.push("Chad")
s.pop()
print(s.peek())
s.pop()
print(s.stack)
