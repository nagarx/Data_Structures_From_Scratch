
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev is None:
                    self.head = current_node.next
                    if current_node.next:
                        current_node.next.prev = None
                else:
                    current_node.prev.next = current_node.next
                    if current_node.next:
                        current_node.next.prev = current_node.prev
                return
            current_node = current_node.next

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next
        return nodes
