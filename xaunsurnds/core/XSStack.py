from collections import deque
from threading import Lock

class Stack:
    """
    A high-performance, thread-safe LIFO (Last In, First Out) stack implementation.
    """

    __slots__ = ("_items", "_lock")

    def __init__(self):
        """Initializes an unbounded, dynamically growing stack with high efficiency."""
        self._items = deque()  # Deque provides O(1) push and pop
        self._lock = Lock()

    def push(self, item):
        """Pushes an item onto the stack with O(1) time complexity."""
        with self._lock:
            self._items.append(item)

    def pop(self):
        """Removes and returns the top item. Raises IndexError if empty."""
        with self._lock:
            if not self._items:
                raise IndexError("pop from empty stack")
            return self._items.pop()

    def peek(self):
        """Returns the top item without removing it, or None if empty."""
        with self._lock:
            return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, otherwise False."""
        with self._lock:
            return not self._items

    def size(self) -> int:
        """Returns the number of items in the stack."""
        with self._lock:
            return len(self._items)

    def clear(self):
        """Removes all items from the stack."""
        with self._lock:
            self._items.clear()

    def bulk_push(self, items):
        """Pushes multiple items onto the stack efficiently."""
        with self._lock:
            if not isinstance(items, (list, tuple)):
                raise TypeError("bulk_push expects a list or tuple of items")
            self._items.extend(items)

    def bulk_pop(self, count: int):
        """Pops multiple items from the stack at once. Raises IndexError if not enough elements."""
        with self._lock:
            if count <= 0:
                raise ValueError("bulk_pop expects a positive integer")
            if count > len(self._items):
                raise IndexError("Not enough elements in stack to pop")
            result = [self._items.pop() for _ in range(count)]
            return result

    def snapshot(self):
        """Returns a snapshot (copy) of the current stack state for safe restoration."""
        with self._lock:
            return list(self._items)

    def restore(self, snapshot):
        """Restores the stack to a previous snapshot state with safety checks."""
        with self._lock:
            if not isinstance(snapshot, list):
                raise TypeError("restore expects a list of items")
            self._items = deque(snapshot)

    def reverse(self):
        """Reverses the order of the stack in-place for optimized traversal."""
        with self._lock:
            self._items.reverse()

    def duplicate_top(self):
        """Duplicates the top element of the stack. Raises IndexError if empty."""
        with self._lock:
            if not self._items:
                raise IndexError("Cannot duplicate top of empty stack")
            self._items.append(self._items[-1])

    def swap_top(self):
        """Swaps the top two elements of the stack. Raises IndexError if fewer than two elements."""
        with self._lock:
            if len(self._items) < 2:
                raise IndexError("Not enough elements to swap top")
            self._items[-1], self._items[-2] = self._items[-2], self._items[-1]

    def contains(self, item) -> bool:
        """Checks if an item exists in the stack in an optimized way."""
        with self._lock:
            return item in self._items

    def __iter__(self):
        """Allows iteration over the stack from top to bottom safely."""
        with self._lock:
            return iter(reversed(self._items))

    def __len__(self) -> int:
        """Returns the size of the stack."""
        return self.size()

    def __repr__(self) -> str:
        """Returns a detailed string representation of the stack for debugging."""
        with self._lock:
            return f"Stack({list(self._items)})"

    def __enter__(self):
        """Allows using the stack in a context manager safely."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Clears the stack when exiting the context manager, ensuring memory safety."""
        self.clear()


class Queue:
    """
    A high-performance, thread-safe FIFO (First In, First Out) queue implementation.
    """

    __slots__ = ("_items", "_lock")

    def __init__(self):
        """Initializes an unbounded, dynamically growing queue with high efficiency."""
        self._items = deque()  # Deque provides O(1) enqueue and dequeue
        self._lock = Lock()

    def enqueue(self, item):
        """Adds an item to the end of the queue with O(1) time complexity."""
        with self._lock:
            self._items.append(item)

    def dequeue(self):
        """Removes and returns the front item. Raises IndexError if empty."""
        with self._lock:
            if not self._items:
                raise IndexError("dequeue from empty queue")
            return self._items.popleft()

    def peek(self):
        """Returns the front item without removing it, or None if empty."""
        with self._lock:
            return self._items[0] if self._items else None

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, otherwise False."""
        with self._lock:
            return not self._items

    def size(self) -> int:
        """Returns the number of items in the queue."""
        with self._lock:
            return len(self._items)

    def clear(self):
        """Removes all items from the queue."""
        with self._lock:
            self._items.clear()

    def bulk_enqueue(self, items):
        """Adds multiple items to the queue efficiently."""
        with self._lock:
            if not isinstance(items, (list, tuple)):
                raise TypeError("bulk_enqueue expects a list or tuple of items")
            self._items.extend(items)

    def bulk_dequeue(self, count: int):
        """Removes multiple items from the queue at once. Raises IndexError if not enough elements."""
        with self._lock:
            if count <= 0:
                raise ValueError("bulk_dequeue expects a positive integer")
            if count > len(self._items):
                raise IndexError("Not enough elements in queue to dequeue")
            result = [self._items.popleft() for _ in range(count)]
            return result

    def snapshot(self):
        """Returns a snapshot (copy) of the current queue state for safe restoration."""
        with self._lock:
            return list(self._items)

    def restore(self, snapshot):
        """Restores the queue to a previous snapshot state with safety checks."""
        with self._lock:
            if not isinstance(snapshot, list):
                raise TypeError("restore expects a list of items")
            self._items = deque(snapshot)

    def reverse(self):
        """Reverses the order of the queue in-place for optimized traversal."""
        with self._lock:
            self._items.reverse()

    def contains(self, item) -> bool:
        """Checks if an item exists in the queue in an optimized way."""
        with self._lock:
            return item in self._items

    def __iter__(self):
        """Allows iteration over the queue from front to back safely."""
        with self._lock:
            return iter(self._items)

    def __len__(self) -> int:
        """Returns the size of the queue."""
        return self.size()

    def __repr__(self) -> str:
        """Returns a detailed string representation of the queue for debugging."""
        with self._lock:
            return f"Queue({list(self._items)})"

    def __enter__(self):
        """Allows using the queue in a context manager safely."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Clears the queue when exiting the context manager, ensuring memory safety."""
        self.clear()
