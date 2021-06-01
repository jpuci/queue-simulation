
class Queue:
    """The queue with the end of the queue at the beginning of the list. [..., third, second, first]"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True, if the queue is empty and False otherwise."""
        return self.items == []

    def enqueue(self, item):
        """Adds item to the end of queue."""
        self.items.insert(0, item)

    def dequeue(self):
        """Removes and returns the first item in the queue."""
        return self.items.pop()

    def size(self):
        """Returns the size of the queue."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the queue."""
        return f'{self.items}'


class ReversedQueue:
    """The queue with the end at the end of the list. [first, second, third, ...] """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True, if the queue is empty and False otherwise."""
        return self.items == []

    def enqueue(self, item):
        """Adds item to the end of queue."""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the first item in the queue."""
        return self.items.pop(0)

    def size(self):
        """Returns the size of the queue."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the queue."""
        return f'{self.items}'
