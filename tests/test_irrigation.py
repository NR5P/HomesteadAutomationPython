import unittest, sys, datetime

sys.path.insert(0,"../src")

from irrigation import Irrigation

class TestIrrigation(unittest.TestCase):
    def test_irrigationCreate(self):
        irrigation1 = Irrigation(3, "barn irrigation", "random notes", 5, [1, 4, 5],{"2020-03-08T01:54:57+0000":"2020-03-08T01:51:57+0000",
                                                                                    "2020-04-08T01:52:51+0000":"2020-03-06T01:54:57+0000"})
        self.assertEqual(irrigation1.pin,5)
        self.assertEqual(irrigation1.name,"barn irrigation")

if __name__ == "__main__":
    unittest.main()