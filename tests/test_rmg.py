#!/usr/bin/env python
import unittest

class TestRmg(unittest.TestCase):
    def setUp(self):
        pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
