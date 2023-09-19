import unittest
from src.Data_Structures.hash_table import HashTable
class TestHashTable(unittest.TestCase):

    def test_insert_search(self):
        hash_table = HashTable()
        hash_table.insert(25, "Apple")
        result = hash_table.search(25)
        self.assertEqual(result, "Apple")

    def test_element_not_found(self):
        hash_table = HashTable()
        result = hash_table.search(100)
        self.assertEqual(result, None)

    def test_update_element(self):
        hash_table = HashTable()
        hash_table.insert(25, "Apple")
        hash_table.insert(25, "Banana")
        result = hash_table.search(25)
        self.assertEqual(result, "Banana")

    def test_collision(self):
        hash_table = HashTable(size=5)
        hash_table.insert(25, "Apple")
        hash_table.insert(30, "Banana")
        result1 = hash_table.search(25)
        result2 = hash_table.search(30)
        self.assertEqual(result1, "Apple")
        self.assertEqual(result2, "Banana")


# Run the test suite
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestHashTable))