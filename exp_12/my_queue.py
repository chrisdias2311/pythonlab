# my_queue.py

class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, value):
        self.queue.append(value)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def rotate(self, n):
        n = n % len(self.queue)
        self.queue = self.queue[n:] + self.queue[:n]
    
    def extend(self, values):
        self.queue.extend(values)
    
    def is_empty(self):
        return len(self.queue) == 0
