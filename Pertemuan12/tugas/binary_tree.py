class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class insert_manual:
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

def traverse_preorder(node):
    if node is not None:
        print(node.data, end=' - ')
        traverse_preorder(node.left)
        traverse_preorder(node.right)

def traverse_inorder(node):
    if node is not None:
        traverse_inorder(node.left)
        print(node.data, end=' - ')
        traverse_inorder(node.right)

def traverse_postorder(node):
    if node is not None:
        traverse_postorder(node.left)
        traverse_postorder(node.right)
        print(node.data, end=' - ')

def get_leaf_nodes(node, leaf_nodes):
    if node is not None:
        if node.left is None and node.right is None:
            leaf_nodes.append(node.data)
        get_leaf_nodes(node.left, leaf_nodes)
        get_leaf_nodes(node.right, leaf_nodes)

tree = insert_manual()

tree.insert_root('A')
tree.insert_left(tree.root, 'B')
tree.insert_right(tree.root, 'C')
tree.insert_left(tree.root.left, 'D')
tree.insert_right(tree.root.left, 'E')
tree.insert_right(tree.root.right, 'F')

def main():
    sep = '=' *  40

    print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
    print(sep)

    print('[INFO] Membangun Struktur Gudang...')
    print('[INFO] Struktur berhasil dibuat.\n')

    print('HASIL AUDIT:')

    print('1. Pre-Order : ', end='')
    traverse_preorder(tree.root)
    print()

    print('2. In-Order : ', end='')
    traverse_inorder(tree.root)
    print()

    print('3. Post-Order : ', end='')
    traverse_postorder(tree.root)
    print('\n')

    leaf_nodes = []
    get_leaf_nodes(tree.root, leaf_nodes)
    print(f'[DATA] Gudang Ujung (Leaf Nodes): {", ".join(leaf_nodes)}')
    print(sep)
    print('Audit Selesai!')

main()