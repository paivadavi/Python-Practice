class Stack:
    
    stack = []
    def __init__(self):
        pass

    def push(self, el):
        # Inserts an element to the beginning of the list
        self.stack.insert(0, el)

    def pop(self):
        # removes an element from the beginning of a list and returns it
        return self.stack.pop(0)

    def peek(self):
        # simply returns the element at the beginning of a list
        return self.stack[0]

    def is_empty(self):
        return len(self.stack) == 0
