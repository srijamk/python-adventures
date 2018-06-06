"""
ID: srijamk1
LANG: PYTHON3
TASK: nocows
"""
import math

content = open('nocows.in').read()
content = content.split(" ")

nodes = int(content[0])
height = int(content[1])

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

def pedigrees():
    s = Stack()
    # Total nodes, height, number of top nodes
    s.push([1, 1, 1, 1])
    count = 0
    while not s.isEmpty():
        top_tree = s.peek()
        if top_tree[0] == nodes and top_tree[1] == height:
            count += top_tree[3]
            s.pop()
        else:
            total_nodes = top_tree[0]
            h = top_tree[1]
            num_nodes = top_tree[2]
            dups = top_tree[3]

            new_list = []
            for n in range(1, num_nodes + 1):
                d = dups * int(math.factorial(num_nodes) / (math.factorial(num_nodes - n) * math.factorial(n)))
                
                if total_nodes + n * 2 <= nodes and h + 1 <= height:
                    new_list.append([total_nodes + n * 2, h + 1, n * 2, d])
            s.pop()
            for lst in new_list:
                s.push(lst)
    return count % 9901

#print(pedigrees())
with open("nocows.out", "w") as g:
    g.write("%i\n" % pedigrees())
