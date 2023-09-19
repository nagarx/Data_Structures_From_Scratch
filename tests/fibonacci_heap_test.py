
import unittest
from src.Data_Structures.fibonacci_heap import Node, FibonacciHeap, insert, extract_min, union, decrease_key, delete_node

class TestFibonacciHeap(unittest.TestCase):

    def test_insert(self):
        heap = FibonacciHeap()
        node1 = Node(3)
        node2 = Node(2)
        insert(heap, node1)
        insert(heap, node2)
        self.assertEqual(heap.min_node.key, 2)

    def test_extract_min(self):
        heap = FibonacciHeap()
        node1 = Node(3)
        node2 = Node(2)
        insert(heap, node1)
        insert(heap, node2)
        self.assertEqual(extract_min(heap).key, 2)

    def test_union(self):
        heap1 = FibonacciHeap()
        heap2 = FibonacciHeap()
        node1 = Node(3)
        node2 = Node(4)
        insert(heap1, node1)
        insert(heap2, node2)
        new_heap = union(heap1, heap2)
        self.assertEqual(new_heap.min_node.key, 3)
        self.assertEqual(new_heap.num_nodes, 2)

    def test_decrease_key(self):
        heap = FibonacciHeap()
        node = Node(3)
        insert(heap, node)
        decrease_key(heap, node, 1)
        self.assertEqual(heap.min_node.key, 1)

    def test_delete_node(self):
        heap = FibonacciHeap()
        node1 = Node(3)
        node2 = Node(2)
        insert(heap, node1)
        insert(heap, node2)
        delete_node(heap, node1)
        self.assertEqual(heap.min_node.key, 2)
        self.assertEqual(heap.num_nodes, 1)

if __name__ == '__main__':
    unittest.main()
