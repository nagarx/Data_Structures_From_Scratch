
# Class to represent a Node in the Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Class to represent the Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None

    # Method to insert a new node
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
                
    # Method for inorder traversal
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        if node:
            if node.left:
                result.extend(self.inorder_traversal(node.left))
            result.append(node.val)
            if node.right:
                result.extend(self.inorder_traversal(node.right))
        return result
    
    # Method to find the minimum value node
    def find_min(self, node=None):
        if node is None:
            node = self.root
        current = node
        while current.left is not None:
            current = current.left
        return current.val
    
    # Method to find the maximum value node
    def find_max(self, node=None):
        if node is None:
            node = self.root
        current = node
        while current.right is not None:
            current = current.right
        return current.val
    
    # Method to delete a node
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, root, key):
        if root is None:
            return root
        
        # Locate the node to be deleted
        if key < root.val:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.val:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Node found, time to delete
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.val = self.find_min(root.right)
            root.right = self._delete_recursive(root.right, root.val)
        
        return root
