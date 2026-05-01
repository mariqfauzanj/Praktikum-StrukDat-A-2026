# Bagian 2: Implementasi Menggunakan Linked List
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None
    
    def push(self, url):
        new_Node = Node(url)
        new_Node.next = self.top
        self.top = new_Node
        self.count += 1

    def pop(self):
        if not self.is_empty():
            url = self.top.url
            self.top = self.top.next
            self.count -= 1
            return url
        else:
            return 'None'

    def peek(self):
        if not self.is_empty():
            return self.top.url
        else:
            return 'None'

    def size(self):
        return self.count
    
stack = StackLinkedList()
print(f'URL  : {stack.peek()}') # peek
print(f'is_Empty: {stack.is_empty()}') # is_empty

stack.push('www.0.com')
stack.push('www.1.com')
stack.push('mafuu.id')
print()

print(f'URL tab: {stack.peek()}') # peek
print(f'Size : {stack.size()}') # size
print(f'is_Empty: {stack.is_empty()}') # is_empty
print()

print(f'Back from {stack.pop()}...') # pop
print()
print(f'URL  : {stack.peek()}') # peek
print(f'Size : {stack.size()}') # size
print(f'is_Empty: {stack.is_empty()}') # is_empty