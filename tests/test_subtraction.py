import unittest
from mypackage.subtraction import subtract

class TestSubtraction(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

if __name__ == '__main__':
    unittest.main()
