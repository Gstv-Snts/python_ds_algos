from typing import Any

from src.DataStructures.LinkedList import Node


class Stack:
    def __init__(self):
        self.head: Node | None = None
        self.length: int = 0

    def push(self, data: Any):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def pop(self) -> Any | None:
        if self.head == None:
            return None
        elif self.length == 1:
            tmp = self.head
            self.head = None
            self.length -= 1
            return tmp.data
        else:
            tmp = self.head
            self.head = tmp.next
            self.length -= 1
            return tmp.data
