
import unittest
from src.doubly_linked_list import DoublyLinkedList
# Define the test suite class
class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_append(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.print_list(), [1, 2, 3])

    def test_prepend(self):
        self.dll.prepend(1)
        self.dll.prepend(2)
        self.dll.prepend(3)
        self.assertEqual(self.dll.print_list(), [3, 2, 1])

    def test_delete_head(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.delete(1)
        self.assertEqual(self.dll.print_list(), [2])

    def test_delete_middle(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.delete(2)
        self.assertEqual(self.dll.print_list(), [1, 3])

    def test_delete_tail(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.delete(2)
        self.assertEqual(self.dll.print_list(), [1])

    def test_search_found(self):
        self.dll.append(1)
        self.dll.append(2)
        self.assertTrue(self.dll.search(1))

    def test_search_not_found(self):
        self.dll.append(1)
        self.dll.append(2)
        self.assertFalse(self.dll.search(3))

if __name__ == "__main__":
    unittest.main()
