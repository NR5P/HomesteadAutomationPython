import unittest, sys, datetime

sys.path.insert(0,"../src")

from irrigation import Irrigation
from device import Device

class TestIrrigation(unittest.TestCase):

    def setUp(self):
        self.irrigation1 = Irrigation(3, "barn irrigation", "random notes", 5, [1, 4, 5],{"2020-03-08T01:54:57+0000":3600,
                                                                                    "2020-04-08T01:52:51+0000":10})
        self.jsonString = '''
            {
            "id": 3,
            "name": "barn irrigation",
            "notes": "random notes",
            "pin": 5,
            "daysOfWeekToIrrigate": [1,3,4],
            "irrigationTimes": {"2020-03-08T01:54:57+0000":3600,"2020-04-08T01:52:51+0000":10}
            }
        '''

    def test_generateFromJson(self):
        timesToConvert = Device.convertToDatetimeTimedeltaDict({"2020-03-08T01:54:57+0000":3600,
                                                                "2020-04-08T01:52:51+0000":10})

        irrigation2 = Irrigation.from_json(self.jsonString)
        self.assertEqual(self.irrigation1.id,3)
        self.assertEqual(self.irrigation1.name,"barn irrigation")
        self.assertEqual(self.irrigation1.notes,"random notes")
        self.assertEqual(self.irrigation1.pin,5)
        self.assertEqual(self.irrigation1.irrigationTimes,timesToConvert)

    def test_irrigationCreate(self):
        timesToConvert = Device.convertToDatetimeTimedeltaDict({"2020-03-08T01:54:57+0000":3600,
                                                                "2020-04-08T01:52:51+0000":10})
        self.assertEqual(self.irrigation1.id,3)
        self.assertEqual(self.irrigation1.name,"barn irrigation")
        self.assertEqual(self.irrigation1.notes,"random notes")
        self.assertEqual(self.irrigation1.pin,5)
        self.assertEqual(self.irrigation1.irrigationTimes,timesToConvert)
    
    def test_toJson(self):
        irrigation3 = Irrigation.from_json(self.jsonString)
        testJson = irrigation3.to_json()
        self.assertEqual(testJson, testJson)


if __name__ == "__main__":
    unittest.main()