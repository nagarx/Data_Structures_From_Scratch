
import unittest
from skip_list import SkipList

class TestSkipList(unittest.TestCase):

    def test_insert(self):
        skip_list = SkipList(4)
        skip_list.insert(3)
        skip_list.insert(6)
        skip_list.insert(7)
        skip_list.insert(9)
        skip_list.insert(12)
        self.assertTrue(skip_list.search(3))
        self.assertTrue(skip_list.search(6))
        self.assertFalse(skip_list.search(5))

    def test_delete(self):
        skip_list = SkipList(4)
        skip_list.insert(3)
        skip_list.insert(6)
        skip_list.insert(7)
        skip_list.delete(6)
        self.assertFalse(skip_list.search(6))
    
    def test_search(self):
        skip_list = SkipList(4)
        skip_list.insert(3)
        skip_list.insert(6)
        self.assertTrue(skip_list.search(3))
        self.assertFalse(skip_list.search(5))
    
    def test_random_level(self):
        skip_list = SkipList(4)
        random_level = skip_list.random_level()
        self.assertTrue(0 <= random_level <= 4)
        
if __name__ == "__main__":
    unittest.main()
