import unittest

from src.DataStructures.Stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack()
        self.assertEqual(0, s.length)
        s.push(10)
        if s.head != None:
            self.assertEqual(10, s.head.data)
        else:
            self.fail()
        self.assertEqual(1, s.length)
        s.push(20)
        if s.head != None:
            self.assertEqual(20, s.head.data)
        else:
            self.fail()
        self.assertEqual(2, s.length)
        s.push(30)
        if s.head != None:
            self.assertEqual(30, s.head.data)
        else:
            self.fail()
        self.assertEqual(3, s.length)

    def test_pop(self):
        s = Stack()
        self.assertEqual(0, s.length)
        s.push(10)
        if s.head != None:
            self.assertEqual(10, s.head.data)
        else:
            self.fail()
        self.assertEqual(1, s.length)
        s.push(20)
        if s.head != None:
            self.assertEqual(20, s.head.data)
        else:
            self.fail()
        self.assertEqual(2, s.length)
        s.push(30)
        if s.head != None:
            self.assertEqual(30, s.head.data)
        else:
            self.fail()
        self.assertEqual(3, s.length)

        self.assertEqual(30, s.pop())
        self.assertEqual(20, s.pop())
        self.assertEqual(10, s.pop())
        self.assertEqual(None, s.pop())


if __name__ == "__main__":
    unittest.main()
