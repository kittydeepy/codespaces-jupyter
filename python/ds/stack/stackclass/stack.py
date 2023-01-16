class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def get_stack(self):
        return self.stack

    def peek(self):
        if self.is_stack_empty():
            return None
        else:
            return self.stack[-1]
    
    def print_stack(self):
        return self.stack

    def is_stack_empty(self):
        return self.stack == [] 