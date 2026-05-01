class QueueArray:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
        print(f'Enqueued: {item}')

    def dequeue(self):
        if self.is_empty():
            return 'Queue kosong'
        removed_item = self.items.pop(0)
        return removed_item
    
    def peek(self):
        if self.is_empty():
            return 'Queue kosong'
        return self.items[0]\
        
    def size(self):
        return len(self.items)