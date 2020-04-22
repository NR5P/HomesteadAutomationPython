import unittest, sys, datetime

sys.path.insert(0,"../src")

from device import Device

class TestDevice(unittest.TestCase):
    def setUp(self):
        self.timeStamp8601 = "2020-04-22T06:08:02+0000"
        self.datetimeFromTimeStamp = datetime.datetime.strptime(self.timeStamp8601,"%Y-%m-%dT%H:%M:%S%z")
        self.secondsOn = 180
        self.timedeltaFromSecondsOn = datetime.timedelta(seconds=self.secondsOn)
        self.timesToConvertDict = {self.timeStamp8601:self.secondsOn}

    def test_convertToDatetimeTimeDeltaDict(self):
        self.dictToTest = {self.datetimeFromTimeStamp:self.timedeltaFromSecondsOn}
        self.assertEqual(Device.convertToDatetimeTimedeltaDict(self.timesToConvertDict),self.dictToTest)

#    def test_convertDatetimeToTimeDelta(self):
#        timeDeltaToTest = datetime.timedelta(hours=2,minutes=42,seconds=3)
#        timeFromMethod = Device.convertISOToTimeDelta("2020-03-08T02:42:03+0000") 
#        self.assertEqual(timeDeltaToTest,timeFromMethod) 

if __name__ == "__main__":
    unittest.main()