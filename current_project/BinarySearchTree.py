class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_recursive(self.root, key)
    
    def insert_recursive(self, node, key):
        if node.key > key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if  node is None or node.key == key:
            return node
        if node.key < key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
        
bst = BinarySearchTree()  # Create a new BST object

# add some nodes
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
# bst.insert(8)
# bst.insert(8)

# search for a key
print(bst.search(11))


        
