import random

class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = Node(None, self.max_level)

    def random_level(self):
        level = 0
        while random.random() < 0.5:
            level += 1
        return min(level, self.max_level)
    
    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.head
        for i in reversed(range(self.max_level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        level = self.random_level()
        new_node = Node(value, level)
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
    
    def delete(self, value):
        update = [None] * (self.max_level + 1)
        current = self.head
        for i in reversed(range(self.max_level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        if current.forward[0] and current.forward[0].value == value:
            delete_level = len(current.forward[0].forward) - 1
            for i in range(delete_level + 1):
                update[i].forward[i] = current.forward[0].forward[i]

    def search(self, value):
        current = self.head
        for i in reversed(range(self.max_level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.value == value:
            return True
        return False
