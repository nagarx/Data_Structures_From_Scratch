
import unittest
from BinaryTree import BinaryTree

# Define the unit test class by inheriting unittest.TestCase
class TestBinaryTree(unittest.TestCase):
    
    def setUp(self):
        self.bt = BinaryTree()
        self.bt.insert(50)
        self.bt.insert(30)
        self.bt.insert(70)
        self.bt.insert(20)
        self.bt.insert(40)
        self.bt.insert(60)
        self.bt.insert(80)
    
    def test_insert(self):
        self.assertEqual(self.bt.inorder_traversal(), [20, 30, 40, 50, 60, 70, 80])
        
    def test_find_min(self):
        self.assertEqual(self.bt.find_min(), 20)
        
    def test_find_max(self):
        self.assertEqual(self.bt.find_max(), 80)
        
    def test_delete(self):
        self.bt.delete(40)
        self.assertEqual(self.bt.inorder_traversal(), [20, 30, 50, 60, 70, 80])
        self.bt.delete(70)
        self.assertEqual(self.bt.inorder_traversal(), [20, 30, 50, 60, 80])
        self.bt.delete(20)
        self.assertEqual(self.bt.inorder_traversal(), [30, 50, 60, 80])

if __name__ == "__main__":
    unittest.main()
