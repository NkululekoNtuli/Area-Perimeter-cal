import unittest
from area_perimeter_cal import*

class Tests(unittest.TestCase):

    def test_get_input(self):
        self.assertEqual(get_input(), "Area: 78.53981633974483" + "\nPerimeter: 31.41592653589793" )
    
    def test_get_input(self):
        self.assertEqual()

if __name__ == "__main__":
    unittest.main()