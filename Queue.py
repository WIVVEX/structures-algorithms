class Queue:
    def __init__(self):
        self.data = []
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        if not self.is_empty():
            a = self.data.pop(0)
            return a
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.data[0]
        return None


