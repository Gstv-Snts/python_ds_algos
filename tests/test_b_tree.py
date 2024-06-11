import unittest

from src.DataStructures.BTree import BTree


class TestBTree(unittest.TestCase):
    def test_insert(self):
        bt = BTree()
        self.assertEqual(bt.length, 0)
        self.assertIsNone(bt.root)

        bt.insert(10)
        self.assertEqual(bt.length, 1)
        self.assertIsNotNone(bt.root)
        if bt.root != None:
            self.assertEqual(bt.root.data, 10)
        else:
            self.fail("root is None")

        bt.insert(5)
        self.assertEqual(bt.length, 2)
        if bt.root.left != None:
            self.assertEqual(bt.root.left.data, 5)
        else:
            self.fail("root.left == None")

        bt.insert(15)
        self.assertEqual(bt.length, 3)
        if bt.root.right != None:
            self.assertEqual(bt.root.right.data, 15)
        else:
            self.fail("root.right == None")

        bt.insert(8)
        self.assertEqual(bt.length, 4)
        if bt.root.left.right != None:
            self.assertEqual(bt.root.left.right.data, 8)
        else:
            self.fail("root.left.right == None")

        bt.insert(3)
        self.assertEqual(bt.length, 5)
        if bt.root.left.left != None:
            self.assertEqual(bt.root.left.left.data, 3)
        else:
            self.fail("root.left.left == None")

        bt.insert(13)
        self.assertEqual(bt.length, 6)
        if bt.root.right.left != None:
            self.assertEqual(bt.root.right.left.data, 13)
        else:
            self.fail("root.right.left == None")

        bt.insert(18)
        self.assertEqual(bt.length, 7)
        if bt.root.right.right != None:
            self.assertEqual(bt.root.right.right.data, 18)
        else:
            self.fail("root.right.right == None")
        bt.print()
