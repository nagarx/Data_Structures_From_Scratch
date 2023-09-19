
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def get_size(self):
        return len(self.items)
