from typing import Any

from src.DataStructures.LinkedList import LinkedList
from src.DataStructures.Stack import Stack


class Node:
    def __init__(self, data):
        self.data: Any | None = data
        self.left: Node | None = None
        self.right: Node | None = None


class BTree:
    def __init__(self):
        self.root: Node | None = None
        self.length: int = 0

    def insert(self, data):
        newNode: Node = Node(data)
        if self.root == None:
            self.root = newNode
            self.length += 1
        else:
            s: Stack = Stack()
            s.push(self.root)
            while s.length > 0:
                curr: Any = s.pop()
                if data <= curr.data:
                    if curr.left == None:
                        curr.left = newNode
                        self.length += 1
                        break
                    else:
                        s.push(curr.left)
                else:
                    if curr.right == None:
                        curr.right = newNode
                        self.length += 1
                        break
                    else:
                        s.push(curr.right)

    def print(self):
        if self.root != None:
            s = Stack()
            s.push(self.root)
            for _ in range(self.length):
                curr = s.pop()
                print(curr.data) if curr != None else print("None")
                if curr != None:
                    if curr.left != None:
                        s.push(curr.left)
                    if curr.right != None:
                        s.push(curr.right)
