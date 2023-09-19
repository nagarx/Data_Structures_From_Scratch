class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.degree = 0

class BinomialHeap:
    def __init__(self):
        self.trees = []

    def merge(self, other):
        self.trees.extend(other.trees)
        self.trees.sort(key=lambda tree: tree.degree)

    def insert(self, key):
        tree = BinomialTree(key)
        heap = BinomialHeap()
        heap.trees.append(tree)
        self.merge(heap)

    def get_min_tree(self):
        if not self.trees:
            return None
        return min(self.trees, key=lambda tree: tree.key)

    def extract_min(self):
        min_tree = self.get_min_tree()
        if min_tree is None:
            return None
        self.trees.remove(min_tree)
        heap = BinomialHeap()
        heap.trees = min_tree.children
        self.merge(heap)
        return min_tree.key

# A simple test to demonstrate the Binomial Heap
heap = BinomialHeap()
heap.insert(3)
heap.insert(7)
heap.insert(1)
heap.insert(4)
heap.insert(9)

# Extract minimum key
min_key = heap.extract_min()
print(min_key)