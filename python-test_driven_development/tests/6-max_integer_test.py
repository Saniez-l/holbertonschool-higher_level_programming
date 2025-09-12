#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_positive_negative(self):
        self.assertEqual(max_integer([-10, -20, -30, -5]), -5)

    def test_list_mixt(self):
        self.assertEqual(max_integer([15, -3, -20, 30, 40]), 40)

    def test_one_element(self):
        self.assertEqual(max_integer([10]), 10)

    def test_list_empty(self):
        self.assertIsNone(max_integer([]))

    def test_list_same_value(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_number(self):
        with self.assertRaises(TypeError):
            TestMaxInteger([1, "S", 3])



if __name__ == '__main__':
    unittest.main()
