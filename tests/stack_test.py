
import unittest
from Stack import Stack
# Define the test suite class
class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.get_size(), 3)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        popped = self.stack.pop()
        self.assertEqual(popped, 2)
        self.assertEqual(self.stack.get_size(), 1)

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)

    def test_is_empty_true(self):
        self.assertTrue(self.stack.is_empty())

    def test_is_empty_false(self):
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

if __name__ == "__main__":
    unittest.main()
