from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        self.previous: Node | None = None


class LinkedList:
    def __init__(self):
        self.head: Node | None
        self.tail: Node | None
        self.length: int = 0

    def insert_at_head(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.head.next = self.tail
            self.tail.previous = self.head
        elif self.length == 1:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insert_at_tail(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.head.next = self.tail
            self.tail.previous = self.head
        elif self.length == 1:
            self.tail = newNode
        else:
            newNode.previous = self.tail
            self.tail = newNode
        self.length += 1

    def pop_head(self) -> Any | None:
        if self.head == None:
            return None
        elif self.length == 1:
            tmp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return tmp.data
        elif self.length == 2:
            tmp = self.head
            self.head = self.tail
            self.length -= 1
            return tmp.data
        else:
            tmp = self.head
            if tmp != None:
                self.head = tmp.next
            self.length -= 1
            return tmp.data

    def pop_tail(self) -> Any | None:
        if self.tail == None:
            return None
        elif self.length == 1:
            tmp = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return tmp.data
        elif self.length == 2:
            tmp = self.tail
            self.tail = self.head
            self.length -= 1
            return tmp.data
        else:
            tmp = self.tail
            if tmp != None:
                self.tail = tmp.previous
            self.length -= 1
            return tmp.data

    def peak_at_head(self) -> Any | None:
        if self.head == None:
            return None
        else:
            return self.head.data

    def peak_at_tail(self) -> Any | None:
        if self.tail == None:
            return None
        else:
            return self.tail.data
