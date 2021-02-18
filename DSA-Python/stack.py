# Stack follows LIFO

from collections import deque

class Stack():
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        self.container.pop()
    
    def peek(self):
        if(self.is_empty()):
            return ("Stack is empty")
        else:
            return self.container[-1]
    
    def is_empty(self):
        return (len(self.container) == 0)
    
    def size(self):
        return len(self.container)

s = Stack()

s.push(5)
print(s.peek())
s.pop()
print(s.peek())
print(s.size())
s.push(67)
s.push(2)
s.push(5)
print(s.peek())
print(s.size())