def enqueue(self, item):
    new_Node = Node(item)
    if self.rear is None:
        self.front = self.rear = new_Node
    else:
        self.rear.next = new_Node
        self.rear = new_Node
    
    self.count += 1
    print(f'Enqueued: {item}')

def dequeue(self):
    if self.is_empty():
        return 'Queue kosong'
    
    temp_data = self.front.data
    self.front = self.front.next

    if self.front is None:
        self.rear = None
    
    self.count -= 1
    return temp_data

def peek(self):
    if self.is_empty():
        return  'Queue kosong'
    return self.front.data

def size(self):
    return self.count

def clear(self):
    self.front = None
    self.rear = None
    self.count = 0