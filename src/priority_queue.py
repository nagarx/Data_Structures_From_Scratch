
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.entry_finder = {}  # mapping of tasks to entries
        self.REMOVED = '<removed-task>'  # placeholder for removed tasks

    def add_task(self, task, priority=0):
        """Add a new task or update the priority of an existing task."""
        if task in self.entry_finder:
            self.remove_task(task)
        entry = [priority, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.queue, entry)

    def remove_task(self, task):
        """Mark an existing task as REMOVED."""
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        """Remove and return the lowest priority task."""
        while self.queue:
            priority, task = heapq.heappop(self.queue)
            if task != self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')
