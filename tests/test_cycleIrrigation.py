import unittest, sys
from freezegun import freezetime

sys.path.insert(0,"../src")

from cycleIrrigation import CycleIrrigation

class TestCycleIrrigation(unittest.TestCase):
    def setUp(self):
        self.cycleIrrigation1 = CycleIrrigation(3, "by barn","random notes", 5, 10, 600, "2020-03-09T19:44:18+0000", "2020-03-09T06:44:18+0000")
        self.jsonString = '{"id": 3,"name": "by barn","notes": "random notes","pin": 5,"cycleOnTime": 10,"cycleOffTime": 600,"blackoutStartTime": "2020-03-09T19:44:18+0000","blackoutStopTime": "2020-03-09T06:44:18+0000"}'

    def test_create(self):
        cycleIrrigation1 = CycleIrrigation(3, "by barn","random notes", 5, 10, 600, "2020-03-09T19:44:18+0000", "2020-03-09T06:44:18+0000")
        self.assertEqual(3, cycleIrrigation1.id)
    
    def test_fromJson(self):
        cycleIrrigation2 = CycleIrrigation.from_json(self.jsonString)
        self.assertEqual(cycleIrrigation2.id, self.cycleIrrigation1.id)
        self.assertEqual(cycleIrrigation2.cycleOnTime,self.cycleIrrigation1.cycleOnTime)
        self.assertEqual(cycleIrrigation2.blackoutStartTime, self.cycleIrrigation1.blackoutStartTime)

    def test_toJson(self):
        jsonTestString = self.cycleIrrigation1.to_json()

#TODO: left off here building test
    def test_isBlackedOut(self):
        duringBlackoutTime = freeze_time("2012-01-14 22:00:00")
        notDuringBlackoutTime = freeze_time("2012-01-14 10:00:00")

        duringBlackoutTime.start()

        duringBlackoutTime.stop()


        notDuringBlackoutTime.start()

        notDuringBlackoutTime.stop()
    

if __name__ == "__main__":
    unittest.main()