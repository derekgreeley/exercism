# circular_buffer.py

class BufferFullException(BufferError):
    """Raised when attempting to write to a full CircularBuffer."""
    pass


class BufferEmptyException(BufferError):
    """Raised when attempting to read from an empty CircularBuffer."""
    pass


class CircularBuffer:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._buf = [None] * capacity
        self._read = 0   # index of next item to read
        self._write = 0  # index of next slot to write
        self._size = 0   # number of stored items

    def read(self):
        if self._size == 0:
            raise BufferEmptyException("Circular buffer is empty")

        value = self._buf[self._read]
        self._buf[self._read] = None
        self._read = (self._read + 1) % self._capacity
        self._size -= 1
        return value

    def write(self, data):
        if self._size == self._capacity:
            raise BufferFullException("Circular buffer is full")

        self._buf[self._write] = data
        self._write = (self._write + 1) % self._capacity
        self._size += 1

    def overwrite(self, data):
        # If not full, overwrite behaves exactly like write.
        if self._size < self._capacity:
            self.write(data)
            return

        # Full: replace the oldest (at read position), then advance both.
        self._buf[self._read] = data
        self._read = (self._read + 1) % self._capacity
        self._write = self._read  # keep write aligned to the next free slot concept

    def clear(self):
        self._buf = [None] * self._capacity
        self._read = 0
        self._write = 0
        self._size = 0
