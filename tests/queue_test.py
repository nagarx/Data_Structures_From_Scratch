
import unittest
from src.queue import Queue
# Define the test suite class
class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.get_size(), 3)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, 1)
        self.assertEqual(self.queue.get_size(), 1)

    def test_front(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.front(), 1)

    def test_is_empty_true(self):
        self.assertTrue(self.queue.is_empty())

    def test_is_empty_false(self):
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())

if __name__ == "__main__":
    unittest.main()
