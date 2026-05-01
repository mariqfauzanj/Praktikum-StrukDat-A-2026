# Bagian 1: Implementasi Menggunakan List Biasa
class StackList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return 'None'

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'None'

    def size(self):
        # dgn len()
        return len(self.items)
    
stack = StackList()
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