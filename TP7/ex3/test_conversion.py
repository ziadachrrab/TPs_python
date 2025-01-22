import unittest
from TP7.ex1.conversion import dollars_to_dirhams, meters_to_kilometers

class TestConversion(unittest.TestCase):

    def test_dollars_to_dirhams(self):
        self.assertEqual(dollars_to_dirhams(1), 10.0)
        self.assertEqual(dollars_to_dirhams(0), 0.0)
        self.assertEqual(dollars_to_dirhams(100), 1000.0)

    def test_meters_to_kilometers(self):
        self.assertEqual(meters_to_kilometers(1000), 1.0)
        self.assertEqual(meters_to_kilometers(0), 0.0)
        self.assertEqual(meters_to_kilometers(5000), 5.0)

if __name__ == "__main__":
    unittest.main()
