class Node: # mwnampung data dan pointer
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree: # menampung node dari BST
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Langkah 1
        new = Node(data)

        # Langkah 2
        if self.root is None:
            # jika ya
            self.root = new
            return
        
        # Langkah 3 (jika tidak, lanjut ini)
        P = self.root
        Q = self.root

        # Langkah 4
        while Q is not None and new.data != P.data:
            # Langkah 5
            P = Q
            
            # Langkah 6
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right

        # Langkah 7
        if new.data == P.data:
            # jika ya
            print('Datanya duplikat')
            return
        
        # Langkah 8
        if new.data < P.data:
            # jika ya
            P.left = new
        # jika tidak    
        else:
            P.right = new

bst = BinarySearchTree()

bst.insert(67)
bst.insert(69)
bst.insert(2006)
bst.insert(911)
bst.insert(2026)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=' -> ')
        in_order(node.right)

in_order(bst.root)
print()

#===============================#

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)
    
    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

tree = BinaryTree()

tree.insert_root('F')
tree.insert_left(tree.root, 'B')
tree.insert_right(tree.root, 'G')
tree.insert_left(tree.root.left, 'A')
tree.insert_right(tree.root.left, 'D')
tree.insert_left(tree.root.left.right, 'C')
tree.insert_right(tree.root.left.right, 'E')
tree.insert_right(tree.root.right, 'I')
tree.insert_left(tree.root.right.right, 'H')

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=' -> ')
        in_order(node.right)

in_order(tree.root)