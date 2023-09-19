# Importing the unittest module for writing test cases
import unittest
from src.avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):

    def test_insert_and_balance(self):
        avl_tree = AVLTree()
        avl_tree.add(30)
        avl_tree.add(20)
        avl_tree.add(40)
        avl_tree.add(10)
        avl_tree.add(5)
        self.assertEqual(avl_tree.root.height, 3)

    def test_empty_tree(self):
        avl_tree = AVLTree()
        self.assertIsNone(avl_tree.root)

    def test_single_element(self):
        avl_tree = AVLTree()
        avl_tree.add(5)
        self.assertEqual(avl_tree.root.key, 5)
        self.assertEqual(avl_tree.root.height, 1)

    def test_multiple_inserts(self):
        avl_tree = AVLTree()
        avl_tree.add(50)
        avl_tree.add(30)
        avl_tree.add(70)
        avl_tree.add(20)
        avl_tree.add(40)
        self.assertEqual(avl_tree.root.key, 50)
        self.assertEqual(avl_tree.root.height, 3)


# Run the test suite
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestAVLTree))
