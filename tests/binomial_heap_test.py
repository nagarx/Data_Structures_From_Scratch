import unittest
from src.Data_Structures.Binomial_Heap import BinomialHeap

class TestBinomialHeap(unittest.TestCase):

    def test_insert_and_extract_min(self):
        heap = BinomialHeap()
        heap.insert(3)
        heap.insert(7)
        heap.insert(1)
        heap.insert(4)
        heap.insert(9)
        self.assertEqual(heap.extract_min(), 1)

    def test_empty_heap(self):
        heap = BinomialHeap()
        self.assertIsNone(heap.extract_min())

    def test_single_element(self):
        heap = BinomialHeap()
        heap.insert(5)
        self.assertEqual(heap.extract_min(), 5)
        self.assertIsNone(heap.extract_min())

    def test_multiple_inserts_and_extracts(self):
        heap = BinomialHeap()
        heap.insert(3)
        heap.insert(2)
        heap.insert(1)
        self.assertEqual(heap.extract_min(), 1)
        self.assertEqual(heap.extract_min(), 2)
        self.assertEqual(heap.extract_min(), 3)
        self.assertIsNone(heap.extract_min())


# Run the test suite
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestBinomialHeap))