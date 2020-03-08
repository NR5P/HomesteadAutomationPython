import unittest, sys, datetime

sys.path.insert(0,"../src")

from device import Device

class TestDevice(unittest.TestCase):
    def test_convertDatetimeToTimeDelta(self):
        timeDeltaToTest = datetime.timedelta(hours=2,minutes=42,seconds=3)
        timeFromMethod = Device.convertISOToTimeDelta("2020-03-08T02:42:03+0000") 
        self.assertEqual(timeDeltaToTest,timeFromMethod) 

if __name__ == "__main__":
    unittest.main()