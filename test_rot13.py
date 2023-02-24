# see https://learn.microsoft.com/en-gb/training/modules/python-get-started-testing/2-python-unittest
import unittest
from rot13 import rot13


class TestAssertions(unittest.TestCase):

    def test_equals(self):
        self.assertEqual("one string", "one string")

    def test_rot13(self):
        self.assertEqual(rot13("Hello World!"), "Uryyb Jbeyq!")


if __name__ == '__main__':
    unittest.main()
