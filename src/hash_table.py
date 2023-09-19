class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    self.table[index].remove(pair)
            self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

# Simple test to demonstrate Hash Table Search
hash_table = HashTable()
hash_table.insert(25, "Apple")
hash_table.insert(35, "Banana")
hash_table.insert(45, "Cherry")

# Search for the value associated with the key 25
result = hash_table.search(25)
print(result)
