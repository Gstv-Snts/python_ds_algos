import unittest

from src.DataStructures.LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_insert_at_head(self):
        ll = LinkedList()
        self.assertEqual(ll.length, 0)

        ll.insert_at_head(10)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 1)

        ll.insert_at_head(20)
        if ll.head != None and ll.tail != None:
            self.assertEqual(20, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 2)

        ll.insert_at_head(30)
        if ll.head != None and ll.tail != None:
            self.assertEqual(30, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 3)

    def test_insert_at_tail(self):
        ll = LinkedList()
        self.assertEqual(ll.length, 0)

        ll.insert_at_tail(10)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 1)

        ll.insert_at_tail(20)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(20, ll.tail.data)
        self.assertEqual(ll.length, 2)

        ll.insert_at_tail(30)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(30, ll.tail.data)
        self.assertEqual(ll.length, 3)

    def test_pop_at_head(self):
        ll = LinkedList()
        self.assertEqual(ll.length, 0)

        ll.insert_at_head(10)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 1)

        ll.insert_at_head(20)
        if ll.head != None and ll.tail != None:
            self.assertEqual(20, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 2)

        ll.insert_at_head(30)
        if ll.head != None and ll.tail != None:
            self.assertEqual(30, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 3)

        self.assertEqual(ll.pop_head(), 30)
        self.assertEqual(ll.pop_head(), 20)
        self.assertEqual(ll.pop_head(), 10)
        self.assertEqual(ll.pop_head(), None)

    def test_pop_at_tail(self):
        ll = LinkedList()
        self.assertEqual(ll.length, 0)

        ll.insert_at_tail(10)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 1)

        ll.insert_at_tail(20)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(20, ll.tail.data)
        self.assertEqual(ll.length, 2)

        ll.insert_at_tail(30)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(30, ll.tail.data)
        self.assertEqual(ll.length, 3)

        self.assertEqual(ll.pop_tail(), 30)
        self.assertEqual(ll.pop_tail(), 20)
        self.assertEqual(ll.pop_tail(), 10)
        self.assertEqual(ll.pop_tail(), None)

    def test_peak_at_head(self):
        ll = LinkedList()
        self.assertEqual(ll.length, 0)

        ll.insert_at_head(10)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 1)

        ll.insert_at_head(20)
        if ll.head != None and ll.tail != None:
            self.assertEqual(20, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 2)

        ll.insert_at_head(30)
        if ll.head != None and ll.tail != None:
            self.assertEqual(30, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 3)

        self.assertEqual(ll.peak_at_head(), 30)
        self.assertEqual(ll.pop_head(), 30)
        self.assertEqual(ll.peak_at_head(), 20)
        self.assertEqual(ll.pop_head(), 20)
        self.assertEqual(ll.peak_at_head(), 10)
        self.assertEqual(ll.pop_head(), 10)
        self.assertEqual(ll.peak_at_head(), None)
        self.assertEqual(ll.pop_head(), None)

    def test_peak_at_tail(self):
        ll = LinkedList()
        self.assertEqual(ll.length, 0)

        ll.insert_at_tail(10)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(10, ll.tail.data)
        self.assertEqual(ll.length, 1)

        ll.insert_at_tail(20)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(20, ll.tail.data)
        self.assertEqual(ll.length, 2)

        ll.insert_at_tail(30)
        if ll.head != None and ll.tail != None:
            self.assertEqual(10, ll.head.data)
            self.assertEqual(30, ll.tail.data)
        self.assertEqual(ll.length, 3)

        self.assertEqual(ll.peak_at_tail(), 30)
        self.assertEqual(ll.pop_tail(), 30)
        self.assertEqual(ll.peak_at_tail(), 20)
        self.assertEqual(ll.pop_tail(), 20)
        self.assertEqual(ll.peak_at_tail(), 10)
        self.assertEqual(ll.pop_tail(), 10)
        self.assertEqual(ll.peak_at_tail(), None)
        self.assertEqual(ll.pop_tail(), None)


if __name__ == "__main__":
    unittest.main()
