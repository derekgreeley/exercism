# linked_list.py

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def push(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self):
        if self.tail is None:
            raise IndexError("List is empty")

        value = self.tail.value

        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1
        return value

    def unshift(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def shift(self):
        if self.head is None:
            raise IndexError("List is empty")

        value = self.head.value

        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.length -= 1
        return value

    def delete(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                if current is self.head and current is self.tail:
                    self.head = self.tail = None
                elif current is self.head:
                    self.head = current.next
                    self.head.prev = None
                elif current is self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.length -= 1
                return

            current = current.next

        raise ValueError("Value not found")