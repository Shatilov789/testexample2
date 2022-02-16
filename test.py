import unittest
from example2 import is_even


class TestUM(unittest.TestCase):

    def testTrue(self):

        result = is_even(10)
        self.assertEqual(result[1], 'Even!')
        self.assertEqual(result[0], True)

    def testFalse(self):
        result = is_even(11)
        self.assertEqual(result[1], 'Odd!')
        self.assertEqual(result[0], False)


if __name__ == '__main__':
    unittest.main()